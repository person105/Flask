from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
def home():
    return render_template("main/index.html")



