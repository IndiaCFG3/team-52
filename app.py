from flask import Flask, render_template, request, redirect, url_for
from helper.create_user import create_user
from helper.validate import validate_user
from constants import students as st_num
from helper.score_converter import list_to_score
from doa.insert import insert_score


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/go_to_login/<login_type>/')
def go_to_login(login_type):
    if login_type == 'school':
        return render_template('principal.html')#TODO add html

    elif login_type == 'organization':
        return render_template('admin.html') #TODO add html

    elif login_type == 'educator':
        return render_template('teacher.html') #TODO add html

    return "Error"


@app.route('/api/organization/create/', methods=['POST'])
def create_organization_main():
    username = request.form['username']
    password = request.form['Password']

    if create_user(username, password, "organization"):
        return render_template('admin.html') #TODO add html

    return "Error! Please try later!"


@app.route('/api/organization/login/', methods=['POST'])
def login_organization_main():
    username = request.form['username']
    password = request.form['password']

    if validate_user(username, password, "organization"):
        return render_template('admin-dashboard.html')  #TODO add html


@app.route('/api/school/create/', methods=['POST'])
def create_school_main():
    username = request.form['username']
    password = request.form['Password']

    if create_user(username, password, "school"):
        return render_template('principal.html')  # TODO add html

    return "Error! Please try later!"


@app.route('/api/school/login/', methods=['POST'])
def login_school_main():
    username = request.form['username']
    password = request.form['password']

    if validate_user(username, password, "school"):
        return render_template('principal-dashboard.html')  # TODO add html

    return "Error! Please try later!"


@app.route('/api/educator/create/', methods=['POST'])
def create_educator_main():
    username = request.form['username']
    password = request.form['Password']

    if create_user(username, password, "educator"):
        return render_template('teacher.html')  # TODO add html

    return "Error! Please try later!"


@app.route('/api/educator/login/', methods=['POST'])
def login_educator_main():
    username = request.form['username']
    password = request.form['password']

    if validate_user(username, password, "educator"):
        return render_template('teacher-dashboard.html')  # TODO add html

    return "Error! Please try later!"


@app.route('/generate/result/', methods=['POST'])
def generate():
    month = request.form['month']
    for i in range(st_num):
        my_list = request.form.getlist('student' + str(i+1))
        score = list_to_score(my_list)
        insert_score(i+1, score, month)

    render_template('teacher-dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)





