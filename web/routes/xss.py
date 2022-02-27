from flask import Blueprint, render_template, request, jsonify, redirect, session, url_for
import hashlib

xss = Blueprint('xss', __name__)

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

            session['user_id'] = rows[0]
            session['username'] = rows[1]
            session['desc'] = rows[4]


            if len(rows) > 0:
                return redirect(url_for('.home'))

            else:
                error = "Invalid username or password!"

        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('naturetemp/login.html', error=error, query= query)


@xss.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        upload()

    if session['username'] is not None:
        return render_template('naturetemp/base.html', username=session['username'], desc=session['desc'])

    else:
        return redirect(url_for('.login'))



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

            #Update session cookies
            if session['username'] == username:
                session['desc'] = desc
            
            print(cur.rowcount, "Record inserted.")
            return redirect(url_for('.home'))


        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('naturetemp/base.html', error=error)


@xss.route('/logout', methods=['GET', 'POST'])
def logout():

    return redirect(url_for('.login'))



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

            # Check if user exists
            query = "select * from users where user_name = %s"
            cur.execute(query,(username))
            rows = cur.fetchall()

            if len(rows) == 0:
                query = "insert into users (user_name,password) values (%s, %s)"
            
                cur.execute(query,(username, hashed.hexdigest()))
                print(query)

                db.connection.commit()
             
                print(cur.rowcount, "Record inserted.")
                return redirect(url_for('.login'))

            else:
                error = "User exists!"

        except Exception as e:
            print(e)
        finally:
            cur.close() 
    
    return render_template('naturetemp/signup.html', error=error)


