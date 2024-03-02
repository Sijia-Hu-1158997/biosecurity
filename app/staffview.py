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

            cursor.execute('SELECT * FROM staff WHERE userid = %s', (session['userid'],))
            staffinfor = cursor.fetchone()
            
            return render_template('staffprofile.html', accountinfor=accountinfor, staffinfor=staffinfor)
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))   



@app.route("/staff_profile/<int:userid>/update_infor", methods=["GET", "POST"])
def update_staff_infor(userid):
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        staff_email = request.form.get('staff_email')
        work_phone_number = request.form.get('work_phone_number')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        cur = getCursor()

        if first_name:
            cur.execute("UPDATE staff SET first_name = %s WHERE userid = %s;", (first_name, userid))
        if last_name:
            cur.execute("UPDATE staff SET last_name = %s WHERE userid = %s;", (last_name, userid))
        if staff_email:
            cur.execute("UPDATE staff SET staff_email = %s WHERE userid = %s;", (staff_email, userid))
        if work_phone_number:
            cur.execute("UPDATE staff SET work_phone_number = %s WHERE userid = %s;", (work_phone_number, userid))
        if username:
            cur.execute("UPDATE secureaccount SET username = %s WHERE userid = %s;", (username, userid))
        if password:
            cur.execute("UPDATE secureaccount SET password = %s WHERE userid = %s;", (password, userid))
        if email:
            cur.execute("UPDATE secureaccount SET email = %s WHERE userid = %s;", (email, userid))

        print ("Information updated successfully!")

        return redirect(url_for('staff_profile'))
    return redirect(url_for('staff_profile'))



@app.route("/listapiarist")
def list_apiarist():
    cursor = getCursor()
    cursor.execute("SELECT * FROM apiarist order by apiarist_id")
    apiaristresult = cursor.fetchall()

    return render_template("apiaristlist.html", apiaristlist = apiaristresult)