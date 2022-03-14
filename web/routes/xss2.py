from secrets import token_urlsafe
from flask import Blueprint, render_template, request, jsonify, redirect, session, url_for, make_response, g, abort

notes = []

xss2 = Blueprint('xss2', __name__)

@xss2.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":

        if(request.form.get('form') is not None):
            add_note(request.form.get('form'))
        
        elif(request.form.get('refresh') is not None):
            reload()


    return render_template('simpletable/base.html', notes = notes)


def reload():
    global notes
    notes = []

def add_note(note):

    notes.append("<tr>                                      \
                        <td>"+str(len(notes)+4)+"</td>      \
                        <td>                                \
                            <br>                            \
                            "+note+"                        \
                            <br><br>                        \
                        </td>                               \
                    </tr>")


