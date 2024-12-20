from typing import Any, Optional
from pydantic import BaseModel

import models

class DetailResponse(BaseModel):
    detail: Optional[str]

class Response(BaseModel):
    status: str

class YachtsResponse(Response):
    yachts: list[models.Yacht]

class YachtResponse(Response):
    yacht: models.Yacht

class OrdersResponse(Response):
    orders: list[models.Order]

class OrderResponse(Response):
    order: models.Order