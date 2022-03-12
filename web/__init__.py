from flask import Flask
from flask_mysqldb import MySQL
import yaml
from flask_pymongo import PyMongo


db = MySQL()

def create_app():
    
    app = Flask(__name__)

    env = yaml.load(open(r'D:\GitAssignment\Flask\Flask\web\db.yaml'))
    app.config['SECRET_KEY'] = env['secret']

    app.config['MYSQL_HOST'] = env['dbhost']
    app.config['MYSQL_USER'] = env['dbuser']
    app.config['MYSQL_PASSWORD'] = env['dbpass']
    app.config['MYSQL_DB'] = env['dbname']

    app.config['MONGO_URI'] = env['mongouri']

    db.init_app(app)
    # mongo.init_app(app)

    from .routes.index import index

    from .routes.sql import sql
    from .routes.sql2 import sql2
    from .routes.noSQL import noSQL

    from .routes.xss import xss
    from .routes.xss2 import xss2
    from .routes.xss3 import xss3

    from .routes.xxe import xxe
    from .routes.xml import xml

    from .routes.insecure import insecure

    app.register_blueprint(index, url_prefix='/')

    app.register_blueprint(sql, url_prefix='/SQL')
    app.register_blueprint(sql2, url_prefix='/SQL2/')
    app.register_blueprint(noSQL, url_prefix='/noSQL/')


    app.register_blueprint(xss, url_prefix='/XSS')
    app.register_blueprint(xss2, url_prefix='/XSS2/')
    app.register_blueprint(xss3, url_prefix='/XSS3/')


    app.register_blueprint(xxe, url_prefix='/XXE')
    app.register_blueprint(xml, url_prefix='/XML')

    app.register_blueprint(insecure, url_prefix='/INSEC')


    return app

mongo = PyMongo(create_app())

