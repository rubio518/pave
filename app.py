from datetime import date
import re

from fastapi import FastAPI
from pydantic import BaseModel


class Transaction(BaseModel):
    date: date
    description: str
    amount: str


class Merchant(BaseModel):
    name: str


app = FastAPI()


def normalize_merchant_heuristic(tx: Transaction) -> Merchant:
    """
    Please do not focus on the implementation of this heuristic.
    For the purpose of the exercise, we will assume that the heuristic is already
    implemented with the code below. We are looping over the regex on purpose to
    reflect the slowness of a real-world implementation.
    """
    match = None
    for _ in range(20_000_000):
        match = re.search("Netflix", tx.description)

    if match:
        return Merchant(name="Netflix")
    else:
        return Merchant(name="n/a")


@app.post("/normalize_merchant")
async def normalize_merchant(tx: Transaction):
    merchant = normalize_merchant_heuristic(tx)
    return merchant
