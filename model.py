
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Admin(db.Model):
    """an admin user"""

    __tablename__ = "admin_users"

    admin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False) 
    password = db.Column(db.String(20), nullable=False)


class Menu_Items(db.Model):
    """menu items"""

    __tablename__ = "menu_items" 

    item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_name = db.Column(db.String(50), nullable=False)
    item_description = db.Column(db.String(200), nullable=True) 
    #item_pic = db.Column('img-url') 
    item_price = db.Column(db.Float,nullable=False)
    item_category = db.Column(db.String, nullable=True) 
    item_time = db.Column(db.Integer, nullable=False)


class Customer(db.Model):
    """customers"""
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), nullable=False, default="guest")
    lname = db.Column(db.String(20), nullable=False, default="guest")
    email = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(20), nullable=True)


class Order(db.Model):
    """online orders for pickup"""
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.customer_id"))
    date_requested = db.Column(db.DateTime)
    total = db.Column(db.Float)
    method = db.Column(db.String(20))


class MenuOrder(db.Model):
    """"menu_item orders"""
    __tablename__ = "menu_orders"

    order_id = db.Column(db.Integer,db.ForeignKey("orders.order_id"), primary_key=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.item_id"))




def connect_to_db(flask_app, db_uri="postgresql:///menu", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

