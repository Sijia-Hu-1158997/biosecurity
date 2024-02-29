from flask import Flask
from flask import render_template
import mysql.connector
from mysql.connector import FieldType
import connect

app = Flask(__name__)

from app import adminview
from app import staffview
from app import apiaristview

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


