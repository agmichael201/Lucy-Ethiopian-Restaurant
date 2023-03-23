from model import db, Admin, Menu_Items, Order, Customer, MenuOrder, connect_to_db



"""ADMIN FUNCTIONS"""

def create_admin(fname, lname, email, password):
    """"Create an admin account."""

    admin = Admin(fname=fname, lname=lname, email=email, password=password)

    return admin 


def get_admins():   
    """Return all admin accounts."""

    return Admin.query.all()


def get_admin_by_email(email):
    """Return an admin by email."""
    print(email)
    return Admin.query.filter(Admin.email == email).first()


def update_admin_name():
    pass






"""MENU_ITEMS_FUNCTIONS"""

def get_menu_items():
    """"Return all menu items."""

    return Menu_Items.query.all() 

def get_menu_items_by_category(item_category):
    """Return all menu items by category"""

    return Menu_Items.query.filter_by(item_category=item_category).all()

def get_menu_item_by_name(item_name):
    """Return menu item by name"""

    item_name = Menu_Items.query.filter(Menu_Items.item_name == item_name).first()


def create_menu_item(item_name, item_description, item_price, item_category, item_time):
    """Create a new menu item"""

    menu_item = Menu_Items(item_name=item_name, item_description=item_description, item_price=item_price, item_category=item_category, item_time=item_time)

    return menu_item


def update_menu_item_name(item_id, new_name):
    """Update menu item name."""

    item = Menu_Items.query.get(item_id)
    item.item_name = new_name


def update_menu_item_description(item_id, new_description):
    """Update menu item description."""

    item = Menu_Items.query.get(item_id)
    item.item_description = new_description 


def update_menu_img():
    pass


def update_menu_item_price(item_id, new_price):
    """Update a menu item price."""

    item = Menu_Items.query.get(item_id)
    item.item_price = new_price


def update_menu_item_category(item_id, new_category):
    """Update menu item category."""

    item = Menu_Items.query.get(item_id)
    item.item_category = new_category


def update_menu_item_time(item_id, new_time):
    """Update menu item category."""

    item = Menu_Items.query.get(item_id)
    item.item_time = new_time




"""ORDERS FUNCTION"""

def get_orders():
    """Show all online orders"""

    return Order.query.all() 


def get_order_by_order_id(order_id):
    """get an order by order_id"""

    return Order.query.get(order_id) 


def create_order(customer_id, date_requested, total, method):
    """create online order"""
 
    order = Order(customer_id=customer_id, date_requested=date_requested, total=total, method=method)

    return order

def get_order_by_customer_id(customer_id):
    """Return list of orders by customer_id"""

    orders = [Order.query.filter_by(customer_id)]

    return orders





"""CUSTOMERS FUNCTIONS"""

def get_customers():
    """Return all customers"""

    return Customer.query.all() 


def get_customer_by_id(customer_id):
    """Return customer by customer_id"""

    return Customer.query.get(customer_id)


def get_customer_by_email(email):
    """Return customer by email"""

    return Customer.query.filter(Customer.email == email).first()




"""MENU_ORDERS FUNCTIONS"""

def get_menu_orders():
    """"Return all menu_item orders"""

    return MenuOrder.query.all()


def get_menu_order_by_order_id(order_id):
    """Return list of menu_orders by order_id"""

    return [MenuOrder.query.filter_by(order_id)]




if __name__ == "__main__":
    from server import app

    connect_to_db(app)



