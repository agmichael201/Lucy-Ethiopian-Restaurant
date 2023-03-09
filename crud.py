from model import db, Admin, Menu, Menu_Items, connect_to_db



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

    return Admin.query.filter(Admin.email == email)


def update_admin_name():
    pass



"""MENU_ITEMS_FUNCTION"""

def get_menu_items():
    """"Return all menu items."""

    return Menu_Items.query.all() 

def get_menu_items_by_category(item_category):
    """Return all menu items by category"""

    return Menu_Items.query.filter_by(item_category=item_category).all()


def create_menu_item(item_name, item_description, item_price, item_category):
    """Create a new menu item"""

    menu_item = Menu_Items(item_name=item_name, item_description=item_description, item_price=item_price, item_category=item_category)

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





"""MENU FUNCTIONS"""

def create_menu(menu_name, menu_change_description):
    """Create a menu."""

    menu = Menu( 
        menu_name=menu_name,
        menu_change_description=menu_change_description,
    )

    return menu


def get_menus():
    """Return all menus."""

    return Menu.query.all()




if __name__ == "__main__":
    from server import app

    connect_to_db(app)



