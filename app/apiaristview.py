from app import app
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


@app.route('/apiarist_profile')
def apiarist_profile():
    if 'loggedin' in session:
        if session['user_type'] == 'apiarist':
            cursor = getCursor()

            cursor.execute('SELECT userid, username, password, email FROM secureaccount WHERE userid = %s', (session['userid'],))
            accountinfor = cursor.fetchone()
            
            cursor.execute('SELECT apiarist_first_name, apiarist_last_name, address, apiarist_email, phone, date_joined FROM biosecurity.apiarist WHERE userid = %s', (session['userid'],))
            apiaristinfor = cursor.fetchone()

            return render_template('apiaristprofile.html', accountinfor=accountinfor, apiaristinfor=apiaristinfor)
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))



# @app.route("/apiarist_profile/<int:userid>/update_infor", methods=["POST"])
# def update_apiarist_infor(userid):
#     if request.method == "POST":
#         connection = getCursor()
#         apiarist_first_name = connection.execute("SELECT apiarist_first_name FROM apiarist")
#         connection.execute("UPDATE apiarist SET apiarist_first_name = %s WHERE userid = %s;", (apiarist_first_name, userid))
        
#         return redirect(url_for('apiarist_profile'), apiarist_first_name = apiarist_first_name)

#     return redirect(url_for('apiarist_profile'))



@app.route("/apiarist_profile/<int:userid>/update_infor", methods=["GET", "POST"])
def update_apiarist_infor(userid):
    if request.method == "POST":
        # Get the form data
        apiarist_first_name = request.form.get('apiarist_first_name')
        apiarist_last_name = request.form.get('apiarist_last_name')
        apiarist_email = request.form.get('apiarist_email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        cur = getCursor()

        if apiarist_first_name:
            cur.execute("UPDATE apiarist SET apiarist_first_name = %s WHERE userid = %s;", (apiarist_first_name, userid))

        if apiarist_last_name:
            cur.execute("UPDATE apiarist SET apiarist_last_name = %s WHERE userid = %s;", (apiarist_last_name, userid))

        if apiarist_email:
            cur.execute("UPDATE apiarist SET apiarist_email = %s WHERE userid = %s;", (apiarist_email, userid))

        if phone:
            cur.execute("UPDATE apiarist SET phone = %s WHERE userid = %s;", (phone, userid))

        if address:
            cur.execute("UPDATE apiarist SET address = %s WHERE userid = %s;", (address, userid))

        if username:
            cur.execute("UPDATE secureaccount SET username = %s WHERE userid = %s;", (username, userid))
        
        if password:
            cur.execute("UPDATE secureaccount SET password = %s WHERE userid = %s;", (password, userid))
        
        if email:
            cur.execute("UPDATE secureaccount SET email = %s WHERE userid = %s;", (email, userid))

        print ("Information updated successfully!")

        return redirect(url_for('apiarist_profile'))
    return redirect(url_for('apiarist_profile'))