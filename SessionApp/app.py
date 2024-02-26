from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "hello"  #this is required for the session

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        userRole = request.form["rl"]
        session["user"] = user       #set the session's user
        session["role"] = userRole   #set the session's user role
        return redirect(url_for("user"))  # redirect to user page
    else:
        if "user" in session: 
            return redirect(url_for("user"))   #if user already logged in

        return render_template("login.html")   
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
    
@app.route("/staff")
def staff():
    if "user" in session:
        if session["role"] == "staff":              #check the role of the user 
            return render_template("staff.html")
        else:
            return "Illegal Access"                 #anyome else other than staff role cannot access
    else:
        return redirect(url_for("login"))
    
@app.route("/admin")
def sadmin():
    if "user" in session:
        if session["role"] == "admin":
            return render_template("admin.html")  #only admin role can access this page
        else:
            return "Illegal Access"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)   #session is cleared at logout
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)