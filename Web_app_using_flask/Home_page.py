from flask import Flask, redirect, render_template, url_for, request, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, current_user
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
FLASK_PORT = 8766
FLASK_HOST = "localhost"

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


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
def home():
    return render_template('login.html', name='login')


@app.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    for user in users:
        if user.username == username and user.password == password:
            return render_template('upload_file.html')
    return "Invalid Credentials"


@app.route('/upload', methods=["GET", "POST"])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(FLASK_HOST, FLASK_PORT)
