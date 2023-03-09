# import json
# import crud
# from model import db, connect_to_db
# from server import app

# connect_to_db(app) 
# with open('data/menu_items.json') as menu_items_data:
#   parsed_json = json.load(menu_items_data)

#   for menu_item in parsed_json:
#       item_name = menu_item["item_name"]
#       item_description = menu_item["item_description"]
#       #item_pic = menu_item["item_pic"]
#       item_price = menu_item["item_price"]
#       item_category = menu_item["item_category"]

#       db_menu_item = crud.create_menu_item(item_name, item_description, item_price, item_category)
#       db.session.add(db_menu_item)

# db.session.commit()


