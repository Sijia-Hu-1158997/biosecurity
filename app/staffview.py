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

@app.route('/staff')
@app.route('/staff/profile')
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



@app.route("/staff/profile/<int:userid>/update_infor", methods=["GET", "POST"])
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



@app.route("/staff/listapiarist")
def list_apiarist():
    cursor = getCursor()
    cursor.execute("SELECT * FROM apiarist order by apiarist_id")
    apiaristresult = cursor.fetchall()

    return render_template("apiaristlist.html", apiaristlist = apiaristresult)

@app.route('/staff/beeinfor')
def staff_bee_infor():
    connection = getCursor()

    sql = """SELECT bee_pests_and_diseases.bee_id, bee_pests_and_diseases.bee_item_type, bee_pests_and_diseases.present_in_nz, bee_pests_and_diseases.common_name, bee_pests_and_diseases.scientific_name, images.image_name, images.image_data
          FROM bee_pests_and_diseases
          JOIN images ON bee_pests_and_diseases.bee_id = images.bee_id;"""

    connection.execute(sql)
    bee_list = connection.fetchall()

    return render_template('staffbeeinfor.html', bee_list = bee_list)




@app.route("/staff/beeinfor/<int:bee_id>", methods=["GET", "POST"])
def update_bee_infor(bee_id):
    connection = getCursor()

    if request.method == "POST":

        a = "SELECT * FROM bee_pests_and_diseases WHERE bee_id = %s;"
        connection.execute(a, (bee_id,))  # Pass bee_id as a tuple

        bee_basic_infor = connection.fetchall()

        b = "SELECT * FROM bee_infor WHERE bee_id = %s;"
        connection.execute(b, (bee_id,))  # Pass bee_id as a tuple
        bee_detail = connection.fetchall()

        c = "SELECT * FROM images WHERE bee_id = %s;"
        connection.execute(c, (bee_id,))  # Pass bee_id as a tuple
        image_list = connection.fetchall()

        bee_id = request.form.get('bee_id')
        bee_item_type = request.form.get('bee_item_type')
        present_in_nz = request.form.get('present_in_nz')
        common_name = request.form.get('common_name')
        scientific_name = request.form.get('scientific_name')
        characteristics = request.form.get('characteristics')
        biology = request.form.get('biology')
        symptoms = request.form.get('symptoms')
        image_name = request.form.get('image_id')
        image_data = request.form.get('image_data')

        cur = getCursor()

        if bee_item_type:
            cur.execute("UPDATE bee_pests_and_diseases SET bee_item_type = %s WHERE bee_id = %s;", (bee_item_type, bee_id,))
        if present_in_nz:
            cur.execute("UPDATE bee_pests_and_diseases SET present_in_nz = %s WHERE bee_id = %s;", (present_in_nz, bee_id,))
        if common_name:
            cur.execute("UPDATE bee_pests_and_diseases SET common_name = %s WHERE bee_id = %s;", (common_name, bee_id,))
        if scientific_name:
            cur.execute("UPDATE bee_pests_and_diseases SET scientific_name = %s WHERE bee_id = %s;", (scientific_name, bee_id,))
        if characteristics:
            cur.execute("UPDATE bee_infor SET characteristics = %s WHERE bee_id = %s;", (characteristics, bee_id,))
        if biology:
            cur.execute("UPDATE bee_infor SET biology = %s WHERE bee_id = %s;", (biology, bee_id,))
        if symptoms:
            cur.execute("UPDATE bee_infor SET symptoms = %s WHERE bee_id = %s;", (symptoms, bee_id,))
        if image_name:
            cur.execute("UPDATE image SET image_name= %s WHERE bee_id = %s;", (image_name, bee_id,))
        if image_data:
            cur.execute("UPDATE image SET image_date = %s WHERE bee_id = %s;", (image_data, bee_id,))

        print ("Information updated successfully!")

        return render_template('managebeeinfor.html',bee_basic_infor = bee_basic_infor, bee_detail = bee_detail, image_list = image_list)

    return render_template('managebeeinfor.html', bee_basic_infor = bee_basic_infor, bee_detail = bee_detail, image_list = image_list)
