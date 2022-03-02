from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
import subprocess as sp
import os, sys

wd = os. getcwd()

xxe = Blueprint('xxe', __name__)

@xxe.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        if request.form.get('res') == 'false':
            test(request.form.get('form'))
            print(sys.argv[1])

        else:
            print(request.form.get('form'))


    return render_template('ext/ramenshop.html')

# @xxe.route('/test.php')
def test(form):
    print(form)
    out = sp.run(["php", wd+r"\php\process.php", form], stdout=sp.PIPE)
    return out.stdout
