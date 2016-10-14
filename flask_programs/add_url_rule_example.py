''' This program says that app.route and app.add_ulr_rule are act as same in the flask.
    Created on 14th Oct 2016
    author : Umesh Kumar
'''

from flask import Flask

app = Flask(__name__)

#
# @app.route('/')
# def index():
#     statement = "This statement is displayed by calling the index function using the app.route method of flask "
#     return statement


def function():
    statement = "This statement is displayed by calling the function using add_url_rule method of flask "
    return statement
app.add_url_rule('/', 'function', function)

if __name__ == "__main__":
    app.run()
