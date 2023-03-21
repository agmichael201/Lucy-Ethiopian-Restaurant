from flask import Flask, render_template, request, flash, session, get_flashed_messages
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/menu_items")
def all_menu_items():
    """View all menu items by category."""

    item_categories = ["Appetizer", "Vegetarian", "Beef", "Lamb", "Chicken", "Drinks" ]

    all_items = {}

    for item_cat in item_categories:
        all_items[item_cat] = crud.get_menu_items_by_category(item_cat) 

    print(all_items)
    return render_template("all_menu_items.html", all_items=all_items )




@app.route("/create_admin", methods=['GET', 'POST'])
def create_admin_account():
    """Create admin account"""
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")
    admin_pin = request.form.get("admin_pin")

    if not fname or not lname or not email or not password or not admin_pin:
        flash("All fields are required.")

        return render_template("create_admin.html", messages=get_flashed_messages())
    
    if admin_pin != "1996":
        flash("Admin pin is incorrect. Please try again.")
        
        return render_template("create_admin.html")

    if crud.get_admin_by_email(email):
        flash("An account with this email already exists, try logging in.")

        return render_template("admin_login.html")
    

    admin = crud.create_admin(fname=request.form.get("fname"), lname=request.form.get("lname"), email=email, password=request.form.get("password"))
    db.session.add(admin)
    db.session.commit()
    flash('Your new admin account has been created! Try logging in now.')
    
    return render_template("admin_login.html", messages=get_flashed_messages())




@app.route("/admin_login", methods=['GET', 'POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    admin = crud.get_admin_by_email(email)
    if admin is None:
        flash("Email or password is incorrect.")
        return render_template("admin_login.html", messages=get_flashed_messages())
    if admin.password != password:
        flash("Email or password is incorrect.")
        return render_template("admin_login.html", messages=get_flashed_messages())
    else:
        session['admin_email'] = admin.email
        flash(f"Welcome back, {admin.fname}!")
        return render_template("admin_user.html", messages=get_flashed_messages())


    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)