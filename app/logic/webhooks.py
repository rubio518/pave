import time
from ..dto.interfaces import Webhook
from redis import Redis
import psycopg2

try:
    conn = psycopg2.connect(
        database="postgres", user="postgres", password="secret",
        host="db", port="5432"
    )
except Exception as e:
    print(e)
    time.sleep(1)
    conn = psycopg2.connect(
        database="postgres", user="postgres", password="secret",
        host="db", port="5432"
    )


redis_con = Redis(host='redis', port=6379)
cur = conn.cursor()


def create_webhook(req: Webhook):
    cur.execute(
        'INSERT INTO public.webhooks (client_id,url) VALUES (%s,%s)',
        (req.client_id, req.url))
    conn.commit()
    redis_con.set(req.client_id, req.url)
    return f"webhook saved for client: {req.client_id}"


def get_webhook(client_id: str) -> Webhook:
    wh = redis_con.get(client_id)
    if(wh):
        return wh
    else:
        print(client_id)
        cur.execute(
            "SELECT url FROM public.webhooks WHERE client_id = %s",
            (client_id,))
        wh_from_db = cur.fetchone()[0]
        if(wh_from_db):
            redis_con.set(client_id, wh_from_db)
            return wh_from_db
