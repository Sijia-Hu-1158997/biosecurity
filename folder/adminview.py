from folder import app
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/admin/dashboard")
def admin_dashboard():

    return ("admin dashboard")


@app.route("/admin/profile")
def admin_profile():

    return ("admin profile")