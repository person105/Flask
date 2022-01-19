from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import hashlib

sql = Blueprint('sql', __name__)

@sql.route('/login', methods=['GET', 'POST'])
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
    
    return render_template('perfagencytemp/login.html', error=error, query= query)


@sql.route('/home', methods=['GET', 'POST'])
def home():

    username = request.args.get('username')
    return render_template('perfagencytemp/base.html', username=username)


@sql.route('/logout', methods=['GET', 'POST'])
def logout():

    return redirect(url_for('.login'))



# @sql.route('/signup', methods=['GET', 'POST'])
# def signup():

#     from ..__init__ import db
#     error = ""
#     query = ""
    
#     if request.method == 'POST':

#         cur = db.connection.cursor()
        
#         try:
#             username = request.form.get('user_name')
#             password = request.form.get('password')

#             print(request.form)

#             hashed = hashlib.md5(password.encode())

#             # Check if user exists
#             query = "select * from users where user_name = '"+username+"'"
#             cur.execute(query)
#             rows = cur.fetchall()

#             if len(rows) == 0:
#                 query = "insert into users (user_name,password) values ('"+username+"','"+hashed.hexdigest()+"')"
            
#                 cur.execute(query)
#                 print(query)

#                 db.connection.commit()
             
#                 print(cur.rowcount, "Record inserted.")
#                 return redirect(url_for('.home', username=username, **request.args))

#             else:
#                 error = "User exists!"

#         except Exception as e:
#             print(e)
#         finally:
#             cur.close() 
    
#     return render_template('perfagencytemp/signup.html', error=error)