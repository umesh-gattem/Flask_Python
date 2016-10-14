" This is sample flask Hello World example. "

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


if __name__ == "__main__":
    app.run()
