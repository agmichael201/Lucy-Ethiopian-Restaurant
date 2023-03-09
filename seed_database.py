import os 
import model
from model import db, connect_to_db
import server
from server import app 
import json
import crud


os.system("dropdb menu")
os.system("createdb menu")


model.connect_to_db(server.app)
model.db.create_all() 

connect_to_db(app) 


# admins_in_db = []
# for admin in admins_data:
#     fname = admin["fname"]
#     lname = admin["lname"]
#     email = admin["email"]
#     password = admin["password"]

#     db_admin = crud.create_admin(fname, lname, email, password)
#     admins_in_db.append(db_admin) 

# model.db.session.add_all(admins_in_db)
# model.db.session.commit()


with open('data/menus.json') as menus_data:
  parsed_json = json.load(menus_data)

  for menu in parsed_json:
      menu_name= menu["menu_name"]
      menu_change_description = menu["menu_change_description"]

      db_menu = crud.create_menu(menu_name, menu_change_description)
      db.session.add(db_menu)

db.session.commit()




with open('data/menu_items.json') as menu_items_data:
  parsed_json = json.load(menu_items_data)

  for menu_item in parsed_json:
      item_name = menu_item["item_name"]
      item_description = menu_item["item_description"]
      #item_pic = menu_item["item_pic"]
      item_price = menu_item["item_price"]
      item_category = menu_item["item_category"]

      db_menu_item = crud.create_menu_item(item_name, item_description, item_price, item_category)
      db.session.add(db_menu_item)

db.session.commit()
