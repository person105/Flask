from email.policy import default
from flask import Blueprint, render_template, request, abort, session, redirect, url_for
import subprocess as sp
import os, sys

wd = os.getcwd()
svr_res = ""
title = ""

xxe = Blueprint('xxe', __name__)

@xxe.route('/', methods=['GET', 'POST'])
def home():
    
    if request.method == 'POST':
        process(request.form.get('form'))
            
    if(request.args.get('res') == "true"):
        set_res(request.args.get('form'))
        set_title(request.args.get('title'))
     
            
    return render_template('ext/ramenshop.html', feedback = svr_res, title = title)


@xxe.route('/flag', methods=['GET', 'POST'])
def flag():

    out = sp.run(["php", wd+r"\php\flag.php"], stdout=sp.PIPE)
    
    return out.stdout

    # abort(401)


# @xxe.route('/pipe', methods=['GET', 'POST'])
def process(form):
    sp.run(["php", wd+r"\php\process.php", form])
    
    # return out.stdout

def set_res(data):
     global svr_res
     svr_res = data

def set_title(data):
     global title
     title = data

