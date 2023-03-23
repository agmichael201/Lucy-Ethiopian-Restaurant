import os 
import model
from model import db, Admin, connect_to_db
import server
from server import app 
import json
import crud


os.system("dropdb menu")
os.system("createdb menu")


model.connect_to_db(server.app)
model.db.create_all() 

connect_to_db(app) 


with open('data/menu_items.json') as menu_items_data:
  parsed_json = json.load(menu_items_data)

  for menu_item in parsed_json:
      item_name = menu_item["item_name"]
      item_description = menu_item["item_description"]
      #item_pic = menu_item["item_pic"]
      item_price = menu_item["item_price"]
      item_category = menu_item["item_category"]
      item_time = menu_item["item_time"]

      db_menu_item = crud.create_menu_item(item_name, item_description, item_price, item_category, item_time)
      db.session.add(db_menu_item)

db.session.commit()



