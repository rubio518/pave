from app.logic.sender import send_notification
from app.dto.interfaces import Merchant, Transaction, Webhook
import re
from app.logic.webhooks import create_webhook as cw
from uuid import uuid4

from fastapi import FastAPI, BackgroundTasks, Header


app = FastAPI()


def normalize_merchant_heuristic(
            tx: Transaction,
            client_id: str,
            request_id: str
        ) -> Merchant:
    """
    Please do not focus on the implementation of this heuristic.
    For the purpose of the exercise, we will assume that the heuristic
    is already implemented with the code below.
    We are looping over the regex on
    purpose to reflect the slowness of a real-world implementation.
    """
    match = None
    for _ in range(20_000_000):
        match = re.search("Netflix", tx.description)

    if match:
        send_notification(client_id, Merchant(name="Netflix"), request_id)
    else:
        send_notification(client_id, Merchant(name="n/a"), request_id)


@app.post("/create_webhook")
async def create_webhook(req: Webhook):
    return cw(req)


@app.post("/normalize_merchant")
async def normalize_merchant(
            tx: Transaction, background_tasks: BackgroundTasks,
            client_id: str = Header(None)
        ):
    request_id = str(uuid4())
    background_tasks.add_task(
        normalize_merchant_heuristic, tx, client_id, request_id
        )
    return {"request_id": request_id}
