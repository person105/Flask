import json
from flask import Blueprint, render_template, request, abort, session, redirect, url_for, jsonify

noSQL = Blueprint('noSQL', __name__)

@noSQL.route('/', methods=['POST','GET'])
def home():

    res = ''
    error = ''

    if request.method == 'POST':

        if (len(request.form) > 0):
            res = check_login(request.form.get('username'), request.form.get('password'))

        elif (len(request.json) > 0):
            params = request.json
            # print("JSON", params)
            res = check_login(params['username'], params['password'])

    if res is not '':
        error = res.json['msg']

        if request.headers['Content-Type'] == 'application/json':
            return res


    return render_template('ext/login.html', error = error)


def check_login(username, password):
    from ..__init__ import mongo

    user = mongo.db.users.find_one({
        "username": username,
        "password": password
    })

    # print(user)

    if user is None:
        return jsonify({'msg': 'User not found.'})
    else:
        return jsonify({'msg': 'User exists!'})


