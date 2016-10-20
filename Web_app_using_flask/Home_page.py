from flask import Flask, redirect, render_template, url_for, request, session, Response, make_response, flash
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required, abort
from werkzeug.utils import secure_filename
import os
import logging
import argparse

app = Flask(__name__)
# FLASK_PORT = 8766
# FLASK_HOST = 'localhost'
# FLASK_HOST = '192.168.48.204'
app.secret_key = os.urandom(32)

app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['GLOBAL_DIR'] = 'static/users'

# PyLogger Initialization
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


users = {
    "umesh": "umesh",
    "prathyush": "prathyush",
    "nandu": "nandu",
    "vinay": "vinay"
}


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.username = None
        self.password = None

    def manager(self, username, password):
        self.username = username
        self.password = password
        return self

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.username, self.password)


users = [User(id).manager(item[0], item[1]) for id, item in enumerate(users.items())]


@app.route('/')
@login_required
def home():
    return render_template("upload_file.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user.username == username and user.password == password:
                login_user(user)
                os.system("mkdir -p " + app.config['GLOBAL_DIR'] + '/' + current_user.username + '/')
                return redirect('/')
        else:
            return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/')
def index():
    return render_template("upload_file.html")


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return users[int(userid)]


@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['GLOBAL_DIR'] + '/' + current_user.username, filename))
        return redirect(url_for('index'))


@app.route('/logout', methods=["GET"])
@login_required
def logout():
    resp = make_response(redirect('/login'))
    session.clear()
    resp.set_cookie('sessionID', expires=0)
    logout_user()
    return resp


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='PyFlow: Debugger')
    # parser.add_argument('-f', '--file', help='Input File for debugging', required=False)
    # parser.add_argument('-r', help="Run Flask", required=True)
    # app.run(host=app.config['FLASK_HOST'], port=app.config['FLASK_PORT'])
    parser = argparse.ArgumentParser(description='PyFlow: Debugger')
    parser.add_argument('-f', '--file', help='Input File for debugging', required=False)
    parser.add_argument('-r', help="Run Flask", required=True)
    args = vars(parser.parse_args())
    if args['r']:
        app.config.from_pyfile(args['r'])
        app.run(host=app.config['FLASK_HOST'], port=app.config['FLASK_PORT'])

