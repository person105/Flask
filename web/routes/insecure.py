from py4j.java_gateway import JavaGateway
from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, make_response
import pickle
import base64


# gateway = JavaGateway()                   # connect to the JVM
# random = gateway.jvm.java.util.Random()

insecure = Blueprint('insecure', __name__)


@insecure.route('/', methods=['GET', 'POST'])
def home():

    if ((request.method == 'POST') ):
        
        func = request.form.get('function')

        if (func == 'encode'):
            return serialize(request.form.get('input'))

        elif (func == 'decode'):
            return deserialize(request.form.get('input'))

    return render_template('space/base.html')



# @insecure.route('/serialize/<input>', methods=['GET', 'POST'])
def serialize(input):

    print(input)
    pickled = pickle.dumps(input)    

    return render_template('space/base.html', encoded = pickled)



# @insecure.route('/deserialize/<input>', methods=['GET', 'POST'])
def deserialize(input):
    
    input = input.replace("'","").replace("b","").encode().decode('unicode_escape')
    print(input)
    binput = input.encode('latin1')

    print(binput)
    deserialized = pickle.loads(binput)

    print(deserialized)
    
    return render_template('space/base.html', decoded = deserialized)



