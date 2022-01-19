from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import hashlib


sql = Blueprint('sql', __name__)

@sql.route('/login', methods=['GET', 'POST'])
def login():

    from ..__init__ import db

    cur = db.connection.cursor()
    error = ""
    query = ""

    if request.method == 'POST':
        
        try:
            username = request.form.get('user_name')
            password = request.form.get('password')

            print(request.form)

            hashed = hashlib.md5(password.encode())

            query = "select * from users where user_name = '"+username+"' and password = '"+hashed.hexdigest()+"' limit 1"
            cur.execute(query)
            print(query)

            rows = cur.fetchall()
            res = jsonify(rows)

            print(rows)

            if len(rows) > 0:
                return redirect(url_for('.home', username=username, **request.args))

            else:
                error = "Invalid username or password!"

        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('login.html', error=error, query= query)


@sql.route('/home', methods=['GET', 'POST'])
def home():

    username = request.args.get('username')
    return render_template('home.html', username=username)


@sql.route('/logout', methods=['GET', 'POST'])
def logout():

    return redirect(url_for('.login'))



@sql.route('/test', methods=['GET', 'POST'])
def test():

    return render_template('perfagencytemp/signup.html')