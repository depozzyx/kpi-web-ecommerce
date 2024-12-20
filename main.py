from typing import Union
from fastapi import FastAPI, HTTPException 

import models
import db
import lib

app = FastAPI(responses={404: {"model": lib.DetailResponse}})


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/yachts/")
async def get_yachts() -> lib.YachtsResponse:
    yachts = db.get_yachts()

    return lib.YachtsResponse(status="ok", yachts=yachts)

@app.post("/yachts/")
async def post_yacht(yacht: models.ChangableYacht) -> lib.Response:
    db.add_yacht(yacht)

    return lib.Response(status="ok")

@app.get("/yachts/{yacht_id}")
async def get_yacht(yacht_id: int) -> lib.YachtResponse:
    yacht = db.get_yacht(yacht_id) 

    return lib.YachtResponse(status="ok", yacht=yacht)

@app.patch("/yachts/{yacht_id}")
async def patch_yacht(yacht_id: int, yacht: models.ChangableYacht) -> lib.Response:
    db.update_yacht(yacht_id, yacht)

    return lib.Response(status="ok")


@app.delete("/yachts/{yacht_id}")
async def delete_yacht(yacht_id: int) -> lib.Response:
    db.delete_yacht(yacht_id)

    return lib.Response(status="ok")


@app.get("/orders/")
async def get_orders() -> lib.OrdersResponse:
    orders = db.get_orders()

    return lib.OrdersResponse(status="ok", orders=orders)

@app.post("/orders/")
async def post_order(order: models.ChangableOrder) -> lib.Response:
    db.add_order(order)

    return lib.Response(status="ok")

@app.get("/orders/{order_id}")
async def get_order(order_id: int) -> lib.OrderResponse:
    order = db.get_order(order_id) 

    return lib.OrderResponse(status="ok", order=order)

@app.patch("/orders/{order_id}")
async def patch_yacht(order_id: int, order: models.ChangableOrder) -> lib.Response:
    db.update_order(order_id, order)

    return lib.Response(status="ok")


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int) -> lib.Response:
    db.delete_order(order_id)

    return lib.Response(status="ok")

