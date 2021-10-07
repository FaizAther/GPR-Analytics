import os

from flask import (
    Flask, redirect, url_for,
    render_template, send_from_directory,
    request, session, flash
)
# Video call dependencies
from flask_socketio import (
    SocketIO, emit, join_room, leave_room
)
from engineio.payload import Payload
from flask import session

from Forms.LoginForm import LoginForm
from Forms.SelectionForm import SelectionForm
from Forms.AddForm import AddForm

from Instution.Run import *

Payload.max_decode_packets = 200

app = Flask(__name__)
app.secret_key = "gpr"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
socketio = SocketIO(app)

# Video chat
_users_in_room = {} # stores room wise user list
_room_of_sid = {} # stores room joined by an used
_name_of_sid = {} # stores display name of users

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    elif 'admin' in session:
        return redirect(url_for('admin'))

    form = LoginForm()
    form.selection.choices = my_sudo.get_selection()
    university = None
    validate = True
    if request.method == "POST":
        university = my_sudo.find_university(form.selection.data)
    if form.validate_on_submit() and university != None:
        session.pop('username', None)
        user = university.find_user(form.username.data)
        validate = user != None and user.validate_password(form.password.data)
        print(validate)
        if validate:
            session['username'] = user.get_id()
            session['university'] = university.get_id()
            if user.get_type() == UserType.ADMIN:
                session.pop('username', None)
                session['admin'] = user.get_id()
                return redirect(url_for('admin'))
            return redirect(url_for('home'))
    return render_template("login.html", form=form, validate=validate)

@app.route('/logout/')
def logout():
    # remove the username from the session if it's there
    if 'username' not in session and 'admin' not in session:
        return redirect(url_for("login"))
    session.pop('username', None)
    session.pop('admin', None)
    session.pop('university', None)
    return redirect(url_for('index'))

@app.route('/home/')
def home():
    if 'username' not in session:
        return redirect(url_for("login"))
    elif 'admin' in session:
        return redirect(url_for('admin'))

    content = my_sudo.find_user(session['university'], session['username'])
    return render_template("home.html", content=content)

@app.route('/engagements/')
def engagements():
    if 'username' in session:
        user = my_sudo.find_user(session['university'], session['username'])
        content = Base.__LIST_STR__(user.get_engagements(), "Engagements=")
    elif 'admin' in session:
        return redirect(url_for('admin'))
    else:
        return redirect(url_for("login"))
    return render_template("home.html", content=content)

@app.route('/university/', methods=['GET', 'POST'])
def university():
    content = "Selection"
    uni_form = SelectionForm()
    #print(my_sudo.get_universities())
    uni_form.selection.choices = my_sudo.get_selection()
    print(my_sudo.get_selection())
    if request.method == 'POST':
        content = BuilderHTML.generate(my_sudo.find_university(uni_form.selection.data))
        print(content)
        #content = uni0.find_faculty(int(path.split("=")[1])).__str__()

    return render_template("university.html", content=content, form=uni_form)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if 'admin' not in session and 'username' not in session:
        return redirect(url_for("login"))
    elif 'admin' not in session:
        return redirect(url_for('home'))
    form = AddForm()
    admin = my_sudo.find_admin(session['university'])
    form.selection.choices = admin.get_functions()
    if request.method == "POST":
        print(form.name.data)
        admin.commit(int(form.selection.data), form.name.data)
    return render_template("admin.html", content=admin, form=form)


def hello(name):
    return render_template("hello.html", content=f"Hello {name}")

@app.route('/public/<file>')
def public(file):
    return send_from_directory(os.path.join(app.root_path, 'public'),
                                file, mimetype='')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# Video chat

@app.route("/video", methods=["GET", "POST"])
def video_index():
    if request.method == "POST":
        room_id = request.form['room_id']
        return redirect(url_for("entry_checkpoint", room_id=room_id))

    return render_template("video_home.html")


@app.route("/room/<string:room_id>/")
def enter_room(room_id):
    if room_id not in session:
        return redirect(url_for("entry_checkpoint", room_id=room_id))
    return render_template("chatroom.html", room_id=room_id, display_name=session[room_id]["name"], mute_audio=session[room_id]["mute_audio"], mute_video=session[room_id]["mute_video"])

@app.route("/room/<string:room_id>/checkpoint/", methods=["GET", "POST"])
def entry_checkpoint(room_id):
    if request.method == "POST":
        display_name = request.form['display_name']
        mute_audio = request.form['mute_audio']
        mute_video = request.form['mute_video']
        session[room_id] = {"name": display_name, "mute_audio":mute_audio, "mute_video":mute_video}
        return redirect(url_for("enter_room", room_id=room_id))

    return render_template("chatroom_checkpoint.html", room_id=room_id)
    

@socketio.on("connect")
def on_connect():
    sid = request.sid
    print("New socket connected ", sid)
    

@socketio.on("join-room")
def on_join_room(data):
    sid = request.sid
    room_id = data["room_id"]
    display_name = session[room_id]["name"]
    
    # register sid to the room
    join_room(room_id)
    _room_of_sid[sid] = room_id
    _name_of_sid[sid] = display_name
    
    # broadcast to others in the room
    print("[{}] New member joined: {}<{}>".format(room_id, display_name, sid))
    emit("user-connect", {"sid": sid, "name": display_name}, broadcast=True, include_self=False, room=room_id)
    
    # add to user list maintained on server
    if room_id not in _users_in_room:
        _users_in_room[room_id] = [sid]
        emit("user-list", {"my_id": sid}) # send own id only
    else:
        usrlist = {u_id:_name_of_sid[u_id] for u_id in _users_in_room[room_id]}
        emit("user-list", {"list": usrlist, "my_id": sid}) # send list of existing users to the new member
        _users_in_room[room_id].append(sid) # add new member to user list maintained on server

    print("\nusers: ", _users_in_room, "\n")


@socketio.on("disconnect")
def on_disconnect():
    sid = request.sid
    room_id = _room_of_sid[sid]
    display_name = _name_of_sid[sid]

    print("[{}] Member left: {}<{}>".format(room_id, display_name, sid))
    emit("user-disconnect", {"sid": sid}, broadcast=True, include_self=False, room=room_id)

    _users_in_room[room_id].remove(sid)
    if len(_users_in_room[room_id]) == 0:
        _users_in_room.pop(room_id)

    _room_of_sid.pop(sid)
    _name_of_sid.pop(sid)

    print("\nusers: ", _users_in_room, "\n")


@socketio.on("data")
def on_data(data):
    sender_sid = data['sender_id']
    target_sid = data['target_id']
    if sender_sid != request.sid:
        print("[Not supposed to happen!] request.sid and sender_id don't match!!!")

    if data["type"] != "new-ice-candidate":
        print('{} message from {} to {}'.format(data["type"], sender_sid, target_sid))
    socketio.emit('data', data, room=target_sid)



if __name__ == "__main__":
    sociio = True    

    if sociio:
        socketio.run(app, debug=True)
    else:
        app.debug = True
        app.run(host="0.0.0.0", port='8888', debug=True)