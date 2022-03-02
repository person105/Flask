from secrets import token_urlsafe
from flask import Blueprint, render_template, request, jsonify, redirect, session, url_for, make_response, g, abort
import hashlib
import os, time

xss = Blueprint('xss', __name__)
auth = False

@xss.route('/login', methods=['GET', 'POST'])
def login():

    from ..__init__ import db
    error = ""
    query = ""

    if request.method == 'POST':
        
        cur = db.connection.cursor()

        try:
            username = request.form.get('user_name')
            password = request.form.get('password')

            print(request.form)

            hashed = hashlib.md5(password.encode())

            query = "select * from users where user_name = %s and password = %s limit 1"
            cur.execute(query,(username, hashed.hexdigest()))
            print(query)

            rows = cur.fetchone()

            if rows is not None:

                session['user_id'] = rows[0]
                session['username'] = rows[1]
                session['desc'] = rows[4]


                print("USER")
                res = make_response(redirect(url_for('.home')))
                res.set_cookie('token', rows[3])
                return res

            else:
                error = "Invalid username or password!"

        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('nature/login.html', error=error, query= query)


@xss.route('/admin', methods=['GET', 'POST'])
def admin():
    
    if request.method == 'POST':
        upload()        

    token = request.cookies.get('token')

    print(token)
    if (token == '8abae5d8bc89622b6bf5a76c948312f2'):
        print("REDIRECT TO ADMIN")
        return render_template('nature/base.html', username="admin", desc="{FLAG: Beware of <script> tag!'}")

    else:
        #TODO: Redirect to UNAUTHORIZED
        
        abort(401)
        return redirect(url_for('.login'))
    

@xss.route('/auth', methods=['GET', 'POST'])
def auth():

    from ..__init__ import db
    cur = db.connection.cursor()

    print(auth)
    if getAuth() == True:
        query = "select * from users where user_name = %s limit 1"
        cur.execute(query,("admin",))
        
        rows = cur.fetchone()
        
        session['user_id'] = rows[0]
        session['username'] = rows[1]
        session['desc'] = rows[4]

        
        res = make_response(redirect(url_for('.admin')))
        res.set_cookie('token', rows[3])
        return res
    
    else:
        return redirect(url_for('.login'))



@xss.route('/home', methods=['GET', 'POST'])
def home():


    if request.method == 'POST':
        upload()

    if session['username'] is not None:
        return render_template('nature/base.html', username=session['username'], desc=session['desc'])

    else:
        return redirect(url_for('.login'))
        

@xss.route('/logout', methods=['GET', 'POST'])
def logout():

    print("LOGOUT")
    session.clear()
    res = make_response(redirect(url_for('.login')))
    res.set_cookie('token', '', expires=0)
    return res



@xss.route('/signup', methods=['GET', 'POST'])
def signup():

    from ..__init__ import db
    error = ""
    query = ""
    
    if request.method == 'POST':

        cur = db.connection.cursor()
        
        try:
            username = request.form.get('user_name')
            password = request.form.get('password')

            print(request.form)

            hashed = hashlib.md5(password.encode())
            cookie = token_urlsafe(16)

            # Check if user exists
            query = "select * from users where user_name = %s limit 1"
            cur.execute(query,(username,))
            rows = cur.fetchall()

            if len(rows) == 0:
                query = "insert into users (user_name,password,cookie) values (%s, %s, %s)"
            
                cur.execute(query,(username, hashed.hexdigest(), cookie))
                print(query)

                db.connection.commit()
             
                print(cur.rowcount, "Record inserted.")
                return redirect(url_for('.login'))

            else:
                print("INVALID")
                error = "User exists!"

        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('nature/signup.html', error=error)

def setAuthTrue():
     global auth
     auth = True

def setAuthFalse():
     global auth
     auth = False

def getAuth():   
     global auth  
     return auth


def upload():

    from ..__init__ import db
    error = ""
    query = ""
    
    if request.method == 'POST':

        cur = db.connection.cursor()
        
        try:
            desc = request.form.get('desc')
            username = request.form.get('user_name')
            print(desc, username)

            query = "UPDATE users SET user_description = %s WHERE user_name = %s"
        
            cur.execute(query,(desc, username))
            print(query)

            db.connection.commit()

            if username == "admin":
                setAuthTrue()
                os.system('docker container run --rm zenika/alpine-chrome --no-sandbox --dump-dom http://host.docker.internal:5000/XSS/auth')

            #Update session cookies
            if session['username'] == username:
                session['desc'] = desc
            
            print(cur.rowcount, "Record inserted.")
            return redirect(url_for('.home'))


        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('nature/base.html', error=error)


