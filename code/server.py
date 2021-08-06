from flask import Flask, redirect, url_for, render_template, send_from_directory
import os

app = Flask(__name__)

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

