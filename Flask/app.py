from flask import Flask, render_template, request, url_for, redirect
from random import randint

import json
import flask_login


username = "fondson";
json_file = "database.json"

# Initialize the Flask application
app = Flask(__name__)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

# Define a route for the default URL, which loads the form
@app.route('/')
def index():

	return render_template('login.html')

@app.route('/sign_in', methods = ['POST'])
def sign_in():
	json_data = open(json_file)
	data = json.load(json_data)
	json_data.close()
	username = request.form["username"]

	if (username in data["user"]
		and request.form["password"] == data['user'][username]['password']):
		return redirect(url_for("user", username = username))
	return redirect(url_for("index"))


@app.route('/<username>')
def user(username):

	return render_template('user.html')

# Run the app :)
if __name__ == '__main__':
  app.run(
        debug=True
  )