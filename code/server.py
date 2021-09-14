import os
from flask_sqlalchemy import SQLAlchemy
from UniQLD import *

from flask import (
    Flask, redirect, url_for,
    render_template, send_from_directory,
    request, session, flash
)

# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

# Video call dependencies
from flask_socketio import (
    SocketIO, emit, join_room, leave_room
)
from engineio.payload import Payload
import flask
from flask import session

Payload.max_decode_packets = 200


DATABASE_NAME = 'gpr.db'

app = Flask(__name__)
app.secret_key = "gpr"



# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

socketio = SocketIO(app)
db = SQLAlchemy(app)

# login_manager = LoginManager()
# login_manager.init_app(app)

# Video chat
_users_in_room = {} # stores room wise user list
_room_of_sid = {} # stores room joined by an used
_name_of_sid = {} # stores display name of users

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.id}, {self.username}')"


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        session.pop('username', None)
        user = uni0.find_user(int(form.username.data))
        valid_pass = user.validate_password(form.password.data)
        print(valid_pass)
        if valid_pass:
            session['username'] = user.get_id()
            return redirect(url_for('home', username=user.get_id()))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/home/<username>')
def home(username):
    if 'username' in session:
        content=uni0.find_user(int(username))
    else:
        content="Not logged in"
    return render_template("home.html", content=content)

@app.route('/engagements/<username>')
def engagements(username):
    if 'username' in session:
        user=uni0.find_user(int(username))
        content = Base.__LIST_STR__(user.get_engagements(), "Engagements=")
    else:
        content="Not logged in"
    return render_template("home.html", content=content)

@app.route('/university/<path>')
def classes(path):
    content = "Not found"
    if path == "UniQLD":
        content = uni0
    elif path.split("=")[0] == "UniQLD-FAC":
        print(path.split("=")[1])
        content = uni0.find_faculty(int(path.split("=")[1])).__str__()
    print(path.split("=")[0])
    return render_template("hello.html", content=content)

@app.route('/public/<file>')
def public(file):
    return send_from_directory(os.path.join(app.root_path, 'public'),
                                file, mimetype='')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return redirect(url_for("hello_world", name="admin"))

@app.route('/show/<name>')
def show_hello(name):
    id = User.query.filter_by(username=name).first()
    return render_template("hello.html", content=f"Hello name={name}, id={id}")

@app.route('/hello/<name>')
def hello_world(name):
    add_user(name)
    return hello(name)

def add_user(name):
    db.session.add(User(id=len(User.query.all()), username=name))
    db.session.commit()

def hello(name):
    return render_template("hello.html", content=f"Hello {name}")


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
        if DATABASE_NAME not in os.listdir():
            db.create_all()
        app.debug = True
        app.run(host="0.0.0.0", port='8888', debug=True)