from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import re
from datetime import datetime
import mysql.connector
from mysql.connector import FieldType
import connect
from flask_hashing import Hashing



app = Flask(__name__)
app.secret_key = 'abcd'

from app import adminview
from app import staffview
from app import apiaristview


hashing = Hashing(app)

dbconn = None
connection = None

def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost,\
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

@app.route("/")
@app.route("/home")
def home():

    return render_template("home.html")




@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        user_password = request.form['password']
    
        username = username.lower()
        # Check if account exists using MySQL
        cursor = getCursor()
        cursor.execute('SELECT * FROM secureaccount WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account is not None:
            password = account[2]
            if hashing.check_value(password, user_password, salt='abcd'):
            # If account exists in accounts table 
            # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['userid'] = account[0]
                session['username'] = account[1]
                session['user_type'] = account[4]
                # Redirect 
                if account[4] == 'staff':
                    return redirect(url_for('staff_profile'))
                elif account[4] == 'apiarist':
                    return redirect(url_for('apiarist_profile'))
                elif account[4] == 'admin':
                    return redirect(url_for('admin_dashboard'))
            else:
                #password incorrect
                msg = 'Incorrect password!'
        else:
            # Account doesnt exist or username incorrect
            msg = 'Incorrect username'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)




@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        apiarist_first_name = request.form['apiarist_first_name']
        apiarist_last_name = request.form['apiarist_last_name']
        address = request.form['address']
        apiarist_email = request.form['apiarist_email']
        phone = request.form['phone']
        username = username.lower()
        current_date = datetime.now().date()
        # Check if account exists using MySQL
        cursor = getCursor()
        cursor.execute('SELECT * FROM secureaccount WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', apiarist_email):
            msg = 'Invalid email address!'
        elif len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
            msg = 'Password must be at least 8 characters long and contain a mix of letters and numbers.'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email or not apiarist_first_name or not apiarist_last_name or not address or not apiarist_email or not phone:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            hashed = hashing.hash_value(password, salt='abcd')
            cursor.execute('INSERT INTO secureaccount (username, password, email) VALUES (%s, %s, %s)', (username, hashed, email,))
            connection.commit()

            cursor.execute('SELECT userid FROM secureaccount WHERE username = %s', (username,))
            userid = cursor.fetchone()[0]

            cursor.execute('INSERT INTO apiarist (userid, apiarist_first_name, apiarist_last_name, address, apiarist_email, phone, date_joined) VALUES (%s, %s, %s, %s, %s, %s, %s)', (userid, apiarist_first_name, apiarist_last_name, address, apiarist_email, phone, current_date,))
            connection.commit()

            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('home'))



@app.route('/references')
def references():
    return render_template('references.html')


