from flask import Flask
from flask_mysqldb import MySQL
import yaml

db = MySQL()


def create_app():
    app = Flask(__name__)

    env = yaml.load(open(r'/var/www/html/Flask/web/db.yaml'))
    app.config['SECRET_KEY'] = env['secret']

    app.config['MYSQL_HOST'] = env['dbhost']
    app.config['MYSQL_USER'] = env['dbuser']
    app.config['MYSQL_PASSWORD'] = env['dbpass']
    app.config['MYSQL_DB'] = env['dbname']

    from .routes.index import index
    from .routes.sql import sql

    db.init_app(app)

    app.register_blueprint(index, url_prefix='/')
    app.register_blueprint(sql, url_prefix='/SQL')


    return app
