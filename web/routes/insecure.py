from py4j.java_gateway import JavaGateway
from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, make_response
import pickle
import base64


# gateway = JavaGateway()                   # connect to the JVM
# random = gateway.jvm.java.util.Random()

insecure = Blueprint('insecure', __name__)


@insecure.route('/', methods=['GET', 'POST'], defaults={'input': None, 'output': None})
def home(input, output):

    if ((request.method == 'POST') or (input != None)):
        if (input != None):
            func = input
        else:
            func = request.form.get('function')

        if (func == 'encode'):
            return redirect(url_for('.serialize', input = request.form.get('input')))

        elif (func == 'decode'):
            return redirect(url_for('.deserialize', input = request.form.get('input')))

    return render_template('space/base.html', data = output)


@insecure.route('/serialize/<input>', methods=['GET', 'POST'])
def serialize(input):

    if request.method == 'POST':
        return redirect(url_for('.home', input = request.form.get('input')))
    
    print(input)
    pickled = pickle.dumps(input)    

    #Deserialize
    return redirect(url_for('.home', output = pickled))



@insecure.route('/deserialize/<input>', methods=['GET', 'POST'])
def deserialize(input):
    
    if request.method == 'POST':
        return redirect(url_for('.home', input = request.form.get('input')))

    print(input)

    data = base64.urlsafe_b64decode(input+'==')
    deserialized = pickle.loads(data)

    print(deserialized)
    

    #Deserialize
    return render_template('space/base.html', data = deserialized)



