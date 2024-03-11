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
        if session['user_type'] == 'staff' or session['user_type'] == 'admin':
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





@app.route('/staff/beeinfor')
def staff_bee_infor():
    connection = getCursor()

    sql = """SELECT bee_pests_and_diseases.bee_id, bee_pests_and_diseases.bee_item_type, bee_pests_and_diseases.present_in_nz, bee_pests_and_diseases.common_name, bee_pests_and_diseases.scientific_name, images.image_name, images.image_data
          FROM bee_pests_and_diseases
          JOIN images ON bee_pests_and_diseases.bee_id = images.bee_id;"""

    connection.execute(sql)
    bee_list = connection.fetchall()

    return render_template('staffbeeinfor.html', bee_list = bee_list)




@app.route("/staff/beeinfor/<int:bee_id>", methods=["GET"])
def view_infor(bee_id):
    connection = getCursor()

    a = "SELECT * FROM bee_pests_and_diseases WHERE bee_id = %s;"
    connection.execute(a, (bee_id,))  
    bee_basic_infor = connection.fetchall()

    b = "SELECT * FROM bee_infor WHERE bee_id = %s;"
    connection.execute(b, (bee_id,)) 
    bee_detail = connection.fetchall()

    c = "SELECT * FROM images WHERE bee_id = %s;"
    connection.execute(c, (bee_id,))  
    image_list = connection.fetchall()

    d = "SELECT * FROM images"
    connection.execute(d)  
    all_image = connection.fetchall()

    return render_template('managebeeinfor.html', bee_basic_infor = bee_basic_infor, bee_detail = bee_detail, image_list = image_list, all_image = all_image)

@app.route("/staff/beeinfor/<int:bee_id>/addphoto", methods=["GET", "POST"])
def add_photo(bee_id):
    if 'loggedin' in session:
        if session['user_type'] == 'admin' or session['user_type'] == 'staff':
            if request.method == "POST":
                image_data = request.form.get('image_data')     
                cur = getCursor()               
                cur.execute("UPDATE images SET image_data = %s WHERE bee_id = %s;", (image_data, bee_id,))
                print("New Data added successfully!")
                return redirect("/staff/beeinfor")
        else:
            return "Illegal Access" 
    else:
        return redirect("/login")
    

@app.route("/staff/beeinfor/<int:bee_id>/update", methods=["GET", "POST"])
def update_bee_infor(bee_id):
    if 'loggedin' in session:
        if session['user_type'] == 'admin' or session['user_type'] == 'staff':
            if request.method == "POST":
                cur = getCursor()
                updated_data = {
                    'bee_item_type': request.form.get('bee_item_type'),
                    'present_in_nz': request.form.get('present_in_nz'),
                    'common_name': request.form.get('common_name'),
                    'scientific_name': request.form.get('scientific_name'),
                    'characteristics': request.form.get('characteristics'),
                    'biology': request.form.get('biology'),
                    'symptoms': request.form.get('symptoms'),
                }
                # Remove empty fields to avoid updating with None
                updated_data = {k: v for k, v in updated_data.items() if v is not None}

                # Update bee_pests_and_diseases table
                for field, value in updated_data.items():
                    if field in ['bee_item_type', 'present_in_nz', 'common_name', 'scientific_name']:
                        cur.execute(f"UPDATE bee_pests_and_diseases SET {field} = %s WHERE bee_id = %s;", (value, bee_id,))
                    if field in ['characteristics', 'biology', 'symptoms']:
                        cur.execute(f"UPDATE bee_infor SET {field} = %s WHERE bee_id = %s;", (value, bee_id,))
                
                print("Information updated successfully!")

                return redirect("/staff/beeinfor")
            
            connection = getCursor()

            a = "SELECT * FROM bee_pests_and_diseases WHERE bee_id = %s;"
            connection.execute(a, (bee_id,))  
            bee_basic_infor = connection.fetchall()

            b = "SELECT * FROM bee_infor WHERE bee_id = %s;"
            connection.execute(b, (bee_id,)) 
            bee_detail = connection.fetchall()

            c = "SELECT * FROM images WHERE bee_id = %s;"
            connection.execute(c, (bee_id,))  
            image_list = connection.fetchall()

            return render_template("managebeeinfor.html", bee_basic_infor = bee_basic_infor, bee_detail = bee_detail, image_list = image_list)
        
        else:
            return "Illegal Access" 

    else:
        return redirect("/login")






@app.route("/staff/beeinfor/add", methods=["GET", "POST"])
def add_bee_infor():
    if 'loggedin' in session:
        if session['user_type'] == 'admin' or session['user_type'] == 'staff':
            if request.method == "POST":
                # Get the form data
                bee_id = request.form.get('bee_id')
                bee_item_type = request.form.get('bee_item_type')
                present_in_nz = request.form.get('present_in_nz')
                common_name = request.form.get('common_name')
                scientific_name = request.form.get('scientific_name')
                characteristics = request.form.get('characteristics')
                biology = request.form.get('biology')
                symptoms = request.form.get('symptoms')
                image_name = request.form.get('image_name')
                image_data = request.form.get('image_data')

                cur = getCursor()

                # Validate required fields
                if not bee_item_type or not present_in_nz or not common_name or not scientific_name or not characteristics or not biology or not symptoms or not image_name:
                    print("All fields are required.")
                else:
                    # Insert the new infor into the database
                    cur = getCursor()

                    cur.execute("INSERT INTO bee_pests_and_diseases (bee_item_type, present_in_nz, common_name, scientific_name) VALUES (%s, %s, %s, %s)",
                                (bee_item_type, present_in_nz, common_name, scientific_name))
                    # Retrieve the auto-generated 'bee_id'
                    cur.execute("SELECT LAST_INSERT_ID()")
                    bee_id = cur.fetchone()[0]

                    # Insert into 'bee_infor' using the retrieved 'bee_id'
                    cur.execute("INSERT INTO bee_infor (bee_id, characteristics, biology, symptoms) VALUES (%s, %s, %s, %s)",
                                (bee_id, characteristics, biology, symptoms))

                    # Insert into 'images' using the retrieved 'bee_id'
                    cur.execute("INSERT INTO images (bee_id, image_name, image_data) VALUES (%s, %s, %s)",
                                (bee_id, image_name, image_data))
                    print("New Data added successfully!")
                    return redirect("/staff/beeinfor/add")
            cur = getCursor()
            d = "SELECT * FROM images"
            cur.execute(d)  
            all_image = cur.fetchall()
            return render_template("staffaddbeeinfor.html", all = all_image)
        else:
            return "Illegal Access" 
    else:
        return redirect("/login")



@app.route("/staff/beeinfor/<int:bee_id>/delete", methods=["POST"])
def delete_bee_infor(bee_id):
    cur = getCursor()

    # Delete from the main table, bee_pests_and_diseases
    cur.execute("DELETE FROM bee_pests_and_diseases WHERE bee_id = %s", (bee_id,))

    print(f"Data for bee_id {bee_id} deleted successfully!")

    # Redirect to the page 
    return redirect(url_for('view_infor', bee_id=bee_id))