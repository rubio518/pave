from pydantic import BaseModel
from datetime import date


class Webhook(BaseModel):
    url: str
    client_id: str


class Transaction(BaseModel):
    date: date
    description: str
    amount: str


class Merchant(BaseModel):
    name: str
