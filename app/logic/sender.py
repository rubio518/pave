from ..dto.interfaces import Merchant
from ..logic.webhooks import get_webhook
import requests


def send_notification(client_id: str, data: Merchant, request_id: str):
    try:
        client = get_webhook(client_id)
        if client is None:
            raise Exception(f"url not found in database for client: {client_id}")
        data = {'merchant': {'name': data.name}, 'request_id': request_id}
        requests.post(client, json=data)
    except Exception as e:
        print("could not send request to client, error:")
        print(e)
