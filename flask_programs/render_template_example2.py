" This program tells the importance of the flask redirect, render template. "

from flask import Flask, redirect, url_for, render_template
username = 'umesh'
app = Flask(__name__)


@app.route('/')
def hello():
    return redirect(url_for('user'))


@app.route('/user')
def user():
    return render_template('index.html', name='umesh')

if __name__ == "__main__":
    app.run()
