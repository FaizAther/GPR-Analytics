import os
from flask import (
    Flask, redirect, url_for,
    render_template, send_from_directory,
    request, session, flash
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "gpr"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

@app.route('/hello/<name>')
def hello_world(name):
    return hello(name)

def hello(name):
    return render_template("hello.html", content=f"Hello {name}")

if __name__ == '__main__':
    app.debug = True
    app.run()
