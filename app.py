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
hashing = Hashing(app)  #create an instance of hashing

# Change this to your secret key (can be anything, it's for extra protection)

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
def home():
    return render_template("home.html")


@app.route("/liststaff")
def liststaff():
    cursor = getCursor()
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    return render_template("stafflist.html", stafflist = result)

@app.route("/listapiarist")
def listapiarist():
    cursor = getCursor()
    cursor.execute("SELECT * FROM apiarist")
    return render_template("home.html")
