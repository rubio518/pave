from ..dto.interfaces import Merchant
from ..logic.webhooks import get_webhook
import requests


def send_notification(client_id: str, data: Merchant, request_id: str):
    print('send notification')
    client = get_webhook(client_id)
    print(client)
    data = {'merchant': {'name': data.name}, 'request_id': request_id}
    response = requests.post(client, json=data)
    print(response)
