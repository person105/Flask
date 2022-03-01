from lib2to3.pgen2 import token
from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, make_response
import hashlib
import sqlite3

sql2 = Blueprint('sql2', __name__)

@sql2.route('/login', methods=['GET', 'POST'])
def login():

    from ..__init__ import db
    cur = db.connection.cursor()
    error = ""


    try:
        if request.method == 'POST':
            username = request.form.get('user_name')
            password = request.form.get('password')

        elif request.method == 'GET':
            username = request.args.get('user_name')
            password = request.args.get('password')

        hashed = hashlib.md5(password.encode())

        cur.execute("SELECT * FROM user WHERE username = '"+username+"' and password = '"+hashed.hexdigest()+"' limit 1")

        rows = cur.fetchone()
        print(rows)
    

        if rows is not None:
            session['username'] = rows[0]
            res = make_response(redirect(url_for('.home')))
            res.set_cookie('token', rows[1])

            return res

        else:
            error = "Invalid username or password!"

    except Exception as e:
        print(e)
    finally:
        cur.close() 
        

    
    return render_template('extentions/sqlogin2.html', error=error)


@sql2.route('/home', methods=['GET', 'POST'])
def home():

    
    if session.get('username') is not None:
        
        return render_template('agency/base.html', username=session['username'], href="/SQL/chap2/logout")

    else:
        return redirect(url_for('.login'))



@sql2.route('/logout', methods=['GET', 'POST'])
def logout():

    session.clear()
    res = make_response(redirect(url_for('.login')))
    res.set_cookie('token', '', domain='127.0.0.1', expires=0)
    return res
