from py4j.java_gateway import JavaGateway
from flask import Blueprint, render_template


# gateway = JavaGateway()                   # connect to the JVM
# random = gateway.jvm.java.util.Random()

insecure = Blueprint('insecure', __name__)


@insecure.route('/')
def home():
    return render_template("sidebar/menu.html")