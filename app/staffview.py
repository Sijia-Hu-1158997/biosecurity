from app import app
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import mysql.connector
from mysql.connector import FieldType
import connect

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


@app.route('/staff_profile')
def staff_profile():
    if 'loggedin' in session:
        if session['user_type'] == 'staff':
            cursor = getCursor()
            
            cursor.execute('SELECT userid, username, password, email FROM secureaccount WHERE userid = %s', (session['userid'],))
            accountinfor = cursor.fetchone()

            cursor.execute('SELECT first_name, last_name, email, work_phone_number, hire_date, position, department FROM biosecurity.staff WHERE userid = %s', (session['userid'],))
            staffinfor = cursor.fetchone()
            
            return render_template('profile.html', accountinfor=accountinfor, staffinfor=staffinfor)
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))   




@app.route("/manage/apiarist", methods = ["GET", "POST"])
def manage_apiarist():
    if request.method == "POST":
        # Get the form data
        apiarist_id = request.form.get('apiarist_id')
        first_name = request.form.get('apiarist.first_name')
        last_name = request.form.get('apiarist.last_name')
        address = request.form.get('apiarist.address')
        email = request.form.get('apiarist.email')
        phone = request.form.get('apiarist.phone')
        date_joined = request.form.get('apiarist.date_joined')
        status = request.form.get('apiarist.status')
        # Validate required fields
        if not first_name or not last_name or not email or not phone:
            print("All fields are required.")
        else:
            # Insert the new apiarist into the database
            cur = getCursor()
            cur.execute("INSERT INTO apiarist (first_name, last_name, address, email, phone, date_joined) VALUES (%s, %s, %s, %s, %s, %s)",
                        (first_name, last_name, address, email, phone, date_joined))
            print ("Apiarist added successfully!")

            # Redirect to the customer list or any other page you prefer
            return redirect("/manage/apiarist")
    return render_template("home.html")









