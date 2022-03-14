from flask import Flask, render_template, url_for, request, redirect, send_from_directory
# from somes import *
import random
import os
import json
import Data

#with open("data.json", "r") as f:
    #tests_data = json.load(f)

tests_data = Data.main_dict

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/tests-list")
def tests_list():
	return render_template("tests-list.html", tests_data=tests_data)

@app.route("/theory")
def theory():
	return render_template("theory.html", theory_data=tests_data)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(405)
def page_not_found(e):
	print(e)
	return render_template('405.html'), 405

@app.route("/блять")
def fuck():
    return '<img width=100% height=100% src="https://sun9-48.userapi.com/impg/sP4QJiTggL_4wCe1f37UTZIUNvNEtFW46WmcJg/bo4YGysf8_M.jpg?size=458x604&quality=96&sign=df3accaf9b858c4d2a1604fb70a8171a&type=album" ></img>'

@app.route("/check/<test_tag>", methods=["POST"])
def check(test_tag):
	user_answers    = []
	correct_answers = []
	if len(request.form) == 0:
		return redirect(f"/test/{test_tag}")
	for i in request.form:
		user_answers.append("".join(request.form.getlist(i)))
	for i in tests_data[test_tag]["tests"]:
		correct_answers.append(i["correct-answer"])

	return render_template("check.html", user_answers=user_answers, correct_answers=correct_answers, tests_data=tests_data, tag=test_tag)


@app.route("/test/<test_tag>")
def test(test_tag):
    if test_tag in tests_data:
        random.shuffle(tests_data[test_tag]["tests"])
        return render_template("test.html", tests_data=tests_data, tag=test_tag)
    return redirect("/tests-list")

if __name__ == "__main__":
	app.run(debug=True)
