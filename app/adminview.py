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

@app.route('/admin_profile')
def admin_profile():
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            cursor = getCursor()
            
            cursor.execute('SELECT userid, username, password, email FROM secureaccount WHERE userid = %s', (session['userid'],))
            accountinfor = cursor.fetchone()

            cursor.execute('SELECT first_name, last_name, email, work_phone_number, hire_date, position, department FROM biosecurity.staff WHERE userid = %s', (session['userid'],))
            staffinfor = cursor.fetchone()

            return render_template('admin.html', accountinfor=accountinfor, staffinfor=staffinfor)
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))



@app.route("/liststaff")
def staff_list():
    cursor = getCursor()
    cursor.execute("SELECT * FROM staff order by staff_number")
    staffresult = cursor.fetchall()

    return render_template("managestaff.html", stafflist = staffresult)


@app.route("/listapiarist")
def list_apiarist():
    cursor = getCursor()
    cursor.execute("SELECT * FROM apiarist order by apiarist_id")
    apiaristresult = cursor.fetchall()

    return render_template("manageapiarist.html", apiaristlist = apiaristresult)