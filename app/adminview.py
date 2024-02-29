from app import app
from flask import render_template
import mysql.connector
from mysql.connector import FieldType
import connect
from flask import request
from flask import redirect
from flask import url_for


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

@app.route("/admin")
@app.route("/admin/dashboard")
def admin_dashboard():

    return "admin dashboard"


@app.route("/admin/profile")
def admin_profile():

    return "admin profile"


@app.route("/liststaff")
def staff_list():
    cursor = getCursor()
    cursor.execute("SELECT * FROM staff order by last_name, first_name asc")
    staffresult = cursor.fetchall()

    return render_template("managestaff.html", stafflist = staffresult)


@app.route("/listapiarist")
def list_apiarist():
    cursor = getCursor()
    cursor.execute("SELECT * FROM apiarist order by apiarist_id")
    apiaristresult = cursor.fetchall()

    return render_template("manageapiarist.html", apiaristlist = apiaristresult)