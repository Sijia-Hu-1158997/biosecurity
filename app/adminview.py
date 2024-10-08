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

@app.route('/admin')
def admin_dashboard():
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            return render_template('admin.html')
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))



@app.route("/liststaff")
def staff_list():
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            cursor = getCursor()
            cursor.execute("SELECT * FROM staff order by staff_number")
            staffresult = cursor.fetchall()
            return render_template("managestaff.html", stafflist = staffresult)
        else:
            return "Illegal Access" 
    else:
        return redirect(url_for('login'))




@app.route("/add/staff", methods = ["GET", "POST"])
def add_staff():
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            if request.method == "POST":
                # Get the form data
                first_name = request.form.get('first_name')
                last_name = request.form.get('last_name')
                staff_email = request.form.get('staff_email')
                work_phone_number = request.form.get('work_phone_number')
                hire_date = request.form.get('hire_date')
                position = request.form.get('position')
                department = request.form.get('department')
                username = request.form.get('username')
                password = request.form.get('password')
                email = request.form.get('email')
                user_type = request.form.get('user_type')
                # Validate required fields
                if not first_name or not last_name or not staff_email or not work_phone_number or not hire_date or not position or not department:
                    print("All fields are required.")
                else:
                    # Insert the new apiarist into the database
                    cur = getCursor()

                    cur.execute("INSERT INTO secureaccount (username, password, email, user_type) VALUES (%s, %s, %s, %s)",
                                (username, password, email, user_type))
                    
                    cur.execute("SELECT LAST_INSERT_ID()")
                    userid = cur.fetchone()[0]
                    
                    cur.execute("INSERT INTO staff (userid, first_name, last_name, staff_email, work_phone_number, hire_date, position, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                (userid, first_name, last_name, staff_email, work_phone_number, hire_date, position, department))
                    print ("Staff added successfully!")

                    # Redirect to the customer list or any other page you prefer
                    return redirect("/liststaff")
        else:
            return "Illegal Access" 
        
    return render_template("manageaddstaff.html")



@app.route("/liststaff/<int:userid>/update", methods=["GET", "POST"])
def admin_update_staff(userid):
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            if request.method == "POST":
        # Get the form data
                first_name = request.form.get('first_name')
                last_name = request.form.get('last_name')
                staff_email = request.form.get('staff_email')
                work_phone_number = request.form.get('work_phone_number')
                hire_date = request.form.get('hire_date')
                position = request.form.get('position')
                department = request.form.get('department')
                staff_status = request.form.get('staff_status')
                cur = getCursor()

                if first_name:
                    cur.execute("UPDATE staff SET first_name = %s WHERE userid = %s;", (first_name, userid))
                if last_name:
                    cur.execute("UPDATE staff SET last_name = %s WHERE userid = %s;", (last_name, userid))
                if staff_email:
                    cur.execute("UPDATE staff SET staff_email = %s WHERE userid = %s;", (staff_email, userid))
                if work_phone_number:
                    cur.execute("UPDATE staff SET work_phone_number = %s WHERE userid = %s;", (work_phone_number, userid))
                if hire_date:
                    cur.execute("UPDATE staff SET hire_date = %s WHERE userid = %s;", (hire_date, userid))
                if position:
                    cur.execute("UPDATE staff SET position = %s WHERE userid = %s;", (position, userid))  
                if department:
                    cur.execute("UPDATE staff SET department = %s WHERE userid = %s;", (department, userid))
                if staff_status:
                    cur.execute("UPDATE staff SET staff_status = %s WHERE userid = %s;", (staff_status, userid))
                print ("Information updated successfully!")
                return redirect("/staff/beeinfor")
            
            cur = getCursor()
            cur.execute("SELECT * FROM staff WHERE userid = %s;", (userid,))
            staff_data = cur.fetchone()
            return render_template("adminupdatestaff.html", userid=userid, staff=staff_data)
        
        else:
            return "Illegal Access" 
    else:
        return redirect("/login")

@app.route("/liststaff/<int:userid>/delete", methods=["POST"])
def delete_staff(userid):
    cur = getCursor()

    cur.execute("DELETE FROM staff WHERE userid = %s", (userid,))

    print(f"Data for userid {userid} deleted successfully!")

    return redirect("/liststaff")


@app.route("/listapiarist")
def list_apiarist():
    cursor = getCursor()
    cursor.execute("SELECT * FROM apiarist order by apiarist_id")
    apiaristresult = cursor.fetchall()

    return render_template("apiaristlist.html", apiaristlist = apiaristresult)

@app.route("/add/apiarist", methods = ["GET", "POST"])
def add_apiarist():
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            if request.method == "POST":
                apiarist_first_name = request.form.get('apiarist_first_name')
                apiarist_last_name = request.form.get('apiarist_last_name')
                apiarist_email = request.form.get('apiarist_email')
                phone = request.form.get('phone')
                address = request.form.get('address')
                date_joined = request.form.get('date_joined')
                username = request.form.get('username')
                password = request.form.get('password')
                email = request.form.get('email')

                print(apiarist_first_name, apiarist_last_name, apiarist_email, phone, date_joined, address, username, password, email)

                # Validate required fields
                if not apiarist_first_name or not apiarist_last_name or not apiarist_email or not phone or not date_joined or not address or not username or not password or not email:
                    print("All fields are required.")
                else:
                    # Insert the new apiarist into the database
                    cur = getCursor()

                    cur.execute("INSERT INTO secureaccount (username, password, email) VALUES (%s, %s, %s)",
                                (username, password, email))
                    
                    cur.execute("SELECT LAST_INSERT_ID()")
                    userid = cur.fetchone()[0]
                    
                    cur.execute("INSERT INTO apiarist (userid, apiarist_first_name, apiarist_last_name, apiarist_email, phone, date_joined, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (userid, apiarist_first_name, apiarist_last_name, apiarist_email, phone, date_joined, address))
                    print ("Apiarist added successfully!")

                    return redirect("/listapiarist")
        else:
            return "Illegal Access" 
        
    return render_template("adminaddapiarist.html")


@app.route("/listapiarist/<int:userid>/update", methods=["GET", "POST"])
def admin_update_apiarist(userid):
    if 'loggedin' in session:
        if session['user_type'] == 'admin':
            if request.method == "POST":
                updated_apiarist_data = {
                    'apiarist_first_name': request.form.get('apiarist_first_name'),
                    'apiarist_last_name': request.form.get('apiarist_last_name'),
                    'apiarist_email': request.form.get('apiarist_email'),
                    'phone': request.form.get('phone'),
                    'address': request.form.get('address'),
                    'date_joined': request.form.get('date_joined'),
                    'status': request.form.get('status'),
                }

                # Remove empty fields to avoid updating with None
                updated_apiarist_data = {k: v for k, v in updated_apiarist_data.items() if v is not None}

                cur = getCursor()
                for field, value in updated_apiarist_data.items():
                    cur.execute(f"UPDATE apiarist SET {field} = %s WHERE userid = %s;", (value, userid,))

                print("Information updated successfully!")

            # Fetch the updated data
            cur = getCursor()
            cur.execute("SELECT * FROM apiarist WHERE userid = %s", (userid,))
            apiaristresult = cur.fetchone()

            return render_template("adminupdateapiarist.html", a=apiaristresult)

        else:
            return "Illegal Access"

    else:
        return redirect("/login")



@app.route("/listapiarist/<int:userid>/delete", methods=["POST"])
def delete_apiarist(userid):
    cur = getCursor()

    cur.execute("DELETE FROM apiarist WHERE userid = %s", (userid,))

    print(f"Data for userid {userid} deleted successfully!")

    return redirect("/listapiarist")