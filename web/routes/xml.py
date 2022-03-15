from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from itsdangerous import json
# import xml.etree.ElementTree as ET
from lxml import etree as ET
import os

wd = os. getcwd()

xml = Blueprint('xml', __name__)

@xml.route('/', methods=['GET', 'POST'])
def home():

    msg = ""
    if request.method == 'POST':

        if len(request.form) > 0:
            res = search(request.form.get('input'))

        elif len(request.args) > 0:
            res = search(request.args.get('input'))

        if request.headers['Content-Type'] == 'application/json':
            return res

        return render_template('ext/spacebase.html', output = res.json['msg'])


    
    return render_template('ext/spacebase.html')

   
def search(input):

    tree = ET.parse(wd+'\data.xml')
    search = tree.xpath('/data//personnel[@name="'+input+'"]')

    if (len(search) > 0):
        return jsonify({'msg' : "Personnel exists."})


    return jsonify({'msg' : "Personnel does not exist."})
        

   


