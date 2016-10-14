from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('main')


@app.route('/main')
def main():
    return redirect('user')


@app.route('/user')
def user():
    return 'Hello world'


with app.test_request_context():
    print(url_for('home'))
    print(url_for('main'))
    print(url_for('user', username='umesh'))

if __name__ == "__main__":
    app.run()
