
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Admin(db.Model):
    """an admin user"""

    __tablename__ = "admin_users"

    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False) 
    password = db.Column(db.String(20), nullable=False)

class Menu(db.Model):
    """menu"""

    __tablename__ = "menus"

    menu_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    menu_name = db.Column(db.String(20), nullable=False)
    menu_change_description  = db.Column(db.String(200), nullable=False)


class Menu_Items(db.Model):
    """menu items"""

    __tablename__ = "menu_items" 

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String(20), nullable=False)
    item_description = db.Column(db.String(200)) 
    #item_pic = db.Column('img-url') 
    item_price = db.Column(db.Float,nullable=False)
    item_category = db.Column(db.String, nullable=True) 
    menu_id = db.Column(db.Integer, db.ForeignKey("menus.menu_id"))




def connect_to_db(flask_app, db_uri="postgresql:///menu", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

