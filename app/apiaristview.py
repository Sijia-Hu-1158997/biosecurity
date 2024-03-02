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


@app.route('/beeinfor')
def bee_infor():
    connection = getCursor()

    sql = """SELECT bee_pests_and_diseases.bee_id, bee_pests_and_diseases.bee_item_type, bee_pests_and_diseases.present_in_nz, bee_pests_and_diseases.common_name, bee_pests_and_diseases.scientific_name, images.image_id, images.image_data
          FROM bee_pests_and_diseases
          JOIN images ON bee_pests_and_diseases.bee_id = images.bee_id;"""

    connection.execute(sql)
    bee_list = connection.fetchall()

    return render_template('beeinfor.html', bee_list = bee_list)



@app.route('/beeinfor/<int:bee_id>')
def view_detail(bee_id):
    connection = getCursor()

    a = "SELECT * FROM bee_pests_and_diseases WHERE bee_id = %s;"
    connection.execute(a, (bee_id,))  # Pass bee_id as a tuple

    bee_basic_infor = connection.fetchall()

    b = "SELECT * FROM bee_infor WHERE bee_id = %s;"
    connection.execute(b, (bee_id,))  # Pass bee_id as a tuple
    bee_detail = connection.fetchall()

    c = "SELECT * FROM images WHERE bee_id = %s;"
    connection.execute(c, (bee_id,))  # Pass bee_id as a tuple
    image_list = connection.fetchall()


    return render_template('viewdetail.html', bee_basic_infor = bee_basic_infor, bee_detail = bee_detail, image_list = image_list)






