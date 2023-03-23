from flask import Flask, render_template, request, flash, session, redirect
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

    if request.method == 'POST':

        if not fname or not lname or not email or not password or not admin_pin:
            flash("Please fill in all boxes.")

            return render_template("create_admin.html")
        
        if admin_pin != "1996":
            flash("Admin pin is incorrect. Please try again.")
            
            return render_template("create_admin.html")

        if crud.get_admin_by_email(email):
            flash("An account with this email already exists, try logging in.")

            return render_template("admin_login.html")
    else:
        return render_template("create_admin.html") 

    admin = crud.create_admin(fname=fname, lname=lname, email=email, password=password)
    db.session.add(admin)
    db.session.commit()
    flash('Your new admin account has been created! Try logging in now.')
    
    return render_template("admin_login.html")




@app.route("/admin_login", methods=['GET', 'POST'])
def login():
    email = request.form.get('email2')
    password = request.form.get('password2')
    print([email])

    admin = crud.get_admin_by_email(email)
    if request.method == 'POST':
        if not email or not password: 
            flash("Please fill in all boxes.")
            return render_template("admin_login.html")
        if admin is None:
            flash("There is not an account associated with this email.")
            return render_template("admin_login.html")
        if admin.password != password:
            flash("Email or password is incorrect.")
            return render_template("admin_login.html")
        else:
            session['admin_email'] = admin.email
            flash(f"Welcome, {admin.fname}!")
            return redirect("/admin_user")
    else:
        return render_template("admin_login.html") 


@app.route("/admin_user", methods=['GET', 'POST'])
def admin_user():
    email = session.get('admin_email')
    admin = crud.get_admin_by_email(email)

    if admin:
        item_categories = ["Appetizer", "Vegetarian", "Beef", "Lamb", "Chicken", "Drinks" ]

        all_items = {}

        for item_cat in item_categories:
            all_items[item_cat] = crud.get_menu_items_by_category(item_cat) 

        return render_template("admin_user.html", admin=admin, all_items=all_items)
    else:
        flash("Please log in as admin to access this page.")
        return redirect("/admin_login")


@app.route("/admin_logout")
def admin_logout():
    session.clear()
    flash("You have been logged out.")
    return redirect ("/admin_login")


    

@app.route("/create_item", methods=['GET', 'POST'])
def create_item():
    item_name = request.form.get("item-name-box")
    item_description = request.form.get("item-description-box")
    item_price = request.form.get("item-price-box")
    item_category = request.form.get("item-category-box")
    item_time = request.form.get("item-time-box")

    if request.method == 'POST':
   
        if not item_name or not item_price or not item_category or not item_time:
            flash("Please fill in all boxes.")
            return render_template("create_item.html")
        
        else: 
            menu_item = crud.create_menu_item(item_name=item_name, item_description=item_description, item_price=item_price, item_category=item_category, item_time=item_time)
            db.session.add(menu_item)
            db.session.commit()
            flash('Your menu item has been added!')
            return redirect ("/admin_user")
    else:
        return render_template("create_item.html")
        

@app.route("/edit_item", methods=['GET', 'POST'])
def edit_item(): 
  pass  



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)