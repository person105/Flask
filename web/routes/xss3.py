from flask import Blueprint, render_template, request, jsonify, redirect, session, url_for, make_response, g, abort
import subprocess as sp
import os

wd = os.getcwd()

xss3 = Blueprint('xss3', __name__)

@xss3.route('/', methods=['GET', 'POST'])
def login():

    data = None
    if request.method == 'POST':
        data = request.form.get('desc')
        # data = sanitize_data(data)

    return render_template('ext/naturehome.html', feedback = data)


@xss3.route('/flag', methods=['GET', 'POST'])
def flag():

    out = sp.run(["php", wd+r"\php\flag4xss3.php"], stdout=sp.PIPE)
    
    return out.stdout

    # abort(401)