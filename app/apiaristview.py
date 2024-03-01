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
            
            cursor.execute('SELECT first_name, last_name, address, email, phone, date_joined FROM biosecurity.apiarist WHERE userid = %s', (session['userid'],))
            apiaristinfor = cursor.fetchone()

            return render_template('apiaristprofile.html', accountinfor=accountinfor, apiaristinfor=apiaristinfor)
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))



