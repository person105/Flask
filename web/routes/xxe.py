from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
import subprocess as sp
import os

wd = os. getcwd()

xxe = Blueprint('xxe', __name__)

@xxe.route('/', methods=['GET', 'POST'])
def home():

    
    return redirect(url_for('.phpex'))

@xxe.route('/test.php')
def phpex():
    out = sp.run(["php", wd+r"\php\test.php"], stdout=sp.PIPE)
    return out.stdout
