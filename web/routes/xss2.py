from secrets import token_urlsafe
from flask import Blueprint, render_template, request, jsonify, redirect, session, url_for, make_response, g, abort

notes = []

xss2 = Blueprint('xss2', __name__)

@xss2.route('/', methods=['GET', 'POST'])
def home():

    global notes
    if request.method == "POST":
        add_note(request.form.get('form'))


    return render_template('simpletable/base.html', notes = notes)

def add_note(note):
    global notes

    #TODO: Check html tag
    notes.append("<tr>                                      \
                        <td>"+str(len(notes)+4)+"</td>      \
                        <td>                                \
                            <br>                            \
                            "+note+"                        \
                            <br><br>                        \
                        </td>                               \
                    </tr>")


