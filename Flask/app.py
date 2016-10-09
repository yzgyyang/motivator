from flask import Flask, render_template, request, url_for, redirect
from random import randint

import json
import flask_login
from flask import jsonify 

username = "fondson";
users_json = "users.json"
tasks_json = "tasks.json"
rewards_json = "rewards.json"

# Initialize the Flask application
app = Flask(__name__)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

# Define a route for the default URL, which loads the form
@app.route('/')
def index():
	return render_template('login.html')

# Authenticates username and password against json data
@app.route('/sign_in', methods = ['POST'])
def sign_in():
	json_data = open(users_json)
	data = json.load(json_data)
	json_data.close()
	
	global username 
	username = request.form["username"]

	if (username in data["user"]
		and request.form["password"] == data['user'][username]['password']):
		return redirect(url_for("user", username = username))
	return redirect(url_for("index"))


@app.route('/<username>')
def user(username):
	print(username)
	user_data = open(users_json)
	data = json.load(user_data)
	role = data["user"][username]["role"]
	user_data.close()
	task_data = open(tasks_json)
	data = json.load(task_data)
	task_data.close();
	t = {"tasks":[]}
	for task in data["tasks"]:
		if task["child"] == username:
			t["tasks"].append(task)
	return render_template('user.html', tasks=t["tasks"], username=username, role=role)
	
# test for jquery
@app.route('/assign/', methods=['GET'])
def assign():
    ret_data = {"todo": request.args.get('todo'),
    			"point": request.args.get('point')}

    task_data = {"child" : "user1"
    , "deadline" : 0
    , "motipoint": ret_data["point"]
    , "name": ret_data["todo"]
    , "parent": "user2"
    , "status": "requested"
    , "submit_time": 0}
    json_data = open(tasks_json)
    data = json.load(json_data)
    data["tasks"].append(task_data)

    with open(tasks_json, 'w') as t:
    	json.dump(data, t)

    return jsonify(ret_data)


# Run the app :)
if __name__ == '__main__':
  app.run(
        debug=True
  )