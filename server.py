from flask import Flask, render_template
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



# @app.route("/menu_items/<item_category>")
# def show_menu_items_by_cat(item_category):
#     """Show menu items by category"""

#     item_category = crud.get_menu_items_by_category(item_category)



#     return render_template("menu_items_cat.html", item_category=item_category)






if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)