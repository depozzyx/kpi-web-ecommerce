from fastapi import HTTPException

import models

yachts = []
last_yacht_id = len(yachts)

def get_yachts():
    global yachts 

    return yachts

def get_yacht(yacht_id: int) -> models.Yacht:
    global yachts

    matches = [yacht for yacht in yachts if yacht.id == yacht_id ]
    if (len(matches) == 0):
        raise HTTPException(404, "yacht with this id not found")
    return matches[0]

def add_yacht(new_yacht: models.ChangableYacht):
    global last_yacht_id, yachts

    last_yacht_id += 1
    yacht = models.Yacht(name=new_yacht.name, capacity=new_yacht.capacity, price_usd=new_yacht.capacity, id=last_yacht_id)
    yachts.append(yacht)

def update_yacht(yacht_id: int, new_yacht: models.ChangableYacht):
    global yachts

    update_data = new_yacht.dict(exclude_unset=True)
    found_data = get_yacht(yacht_id).dict()
    found_data.update(update_data)

    new_yacht = models.Yacht(**found_data)


    yachts = [yacht if yacht.id != yacht_id else new_yacht for yacht in yachts]

def delete_yacht(yacht_id: int):
    global yachts

    yachts = [yacht for yacht in yachts if yacht.id != yacht_id]



orders = []
last_order_id = len(orders)

def get_orders():
    global orders 

    return orders

def get_order(order_id: int) -> models.Order:
    global orders

    matches = [order for order in orders if order.id == order_id ]
    if (len(matches) == 0):
        raise HTTPException(404, "order with this id not found")
    return matches[0]

def add_order(new_order: models.ChangableOrder):
    global last_order_id, orders

    last_order_id += 1
    order = models.Order(yacht=get_yacht(new_order.yacht_id), client_phone=new_order.client_phone, id=last_order_id)
    orders.append(order)

def update_order(order_id: int, new_order: models.ChangableYacht):
    global orders

    update_data = new_order.dict(exclude_unset=True)
    if ("yacht_id" in update_data):
        update_data["yacht"] = get_yacht(update_data.pop("yacht_id")) 
        
    found_data = get_order(order_id).dict()
    found_data.update(update_data)

    new_order = models.Order(**found_data)


    orders = [order if order.id != order_id else new_order for order in orders]

def delete_order(order_id: int):
    global orders

    orders = [order for order in orders if order.id != order_id]