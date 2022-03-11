import json
from flask import Blueprint, render_template, request, abort, session, redirect, url_for, jsonify

noSQL = Blueprint('noSQL', __name__)

@noSQL.route('/', methods=['POST','GET'])
def home():

    if request.method == 'POST':
        if (request.form is not None):
            return check_login(request.form.get('username'), request.form.get('password'))

    if request.method == 'GET':
        if (request.json is not None):
            params = request.json
            print(params)
            return check_login(params['username'], params['password'])


    return render_template('ext/login.html')


def check_login(username, password):
    from ..__init__ import mongo

    user = mongo.db.users.find_one({
        "username": username,
        "password": password
    })

    print(user)

    if user is None:
        return jsonify({'msg': 'User not found.'})
    else:
        return jsonify({'msg': 'User exists!'})


