from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
# import xml.etree.ElementTree as ET
from lxml import etree as ET
import os

wd = os. getcwd()

xml = Blueprint('xml', __name__)

@xml.route('/', methods=['GET', 'POST'])
def home():

    msg = ""
    if request.method == 'POST':
        return search(request.form.get('input'))

    
    return render_template('ext/spacebase.html')

   
def search(input):
    msg = ""
    tree = ET.parse(wd+'\data.xml')
    search = tree.xpath('/data//personnel[@name="'+input+'"]')

    if (len(search) > 0):
        msg = "Personnel exists."

    else:
        msg = "Personnel does not exist."

    return render_template('ext/spacebase.html', output = msg)

   


