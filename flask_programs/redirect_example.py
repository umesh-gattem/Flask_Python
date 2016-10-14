" This program tells the importance of the flask redirect. "

from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/')
def hello():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return 'Login'

if __name__ == "__main__":
    app.run()
