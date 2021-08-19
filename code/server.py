import os
from flask import (
    Flask, redirect, url_for,
    render_template, send_from_directory,
    request, session, flash
)
from flask_sqlalchemy import SQLAlchemy

DATABASE_NAME = 'gpr.db'

app = Flask(__name__)
app.secret_key = "gpr"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.id}, {self.username}')"

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

@app.route('/video')
def video():
    return render_template("video.html")

if __name__ == '__main__':
    if DATABASE_NAME not in os.listdir():
        db.create_all()
    app.debug = True
    app.run(host="0.0.0.0", port='8888', debug=True)
