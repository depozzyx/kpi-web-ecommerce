from typing import Optional
from pydantic import BaseModel

class ChangableYacht(BaseModel):
    name: Optional[str] = None
    capacity: Optional[int] = None
    price_usd: Optional[float] = None

class Yacht(ChangableYacht):
    id: int

class ChangableOrder(BaseModel):
    yacht_id: Optional[int] = None
    client_phone: Optional[str] = None

class Order(BaseModel):
    yacht: Yacht
    client_phone: str
    id: int
