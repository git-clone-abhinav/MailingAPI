import time
import os
from dotenv import load_dotenv
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.from_url("https://discord.com/api/webhooks/922134536605814826/_JWxho2p4cQFE54yWfFMmJwh57kpSo7kgWH5Z3RcznVhYd2JSyQm7cXhprNgfmhMFjvO", adapter=RequestsWebhookAdapter())
load_dotenv()
logPath = os.getenv('logs')
def log_it(message):
    webhook.send(message)
    with open(logPath, 'a') as f:
        f.write(f"{time.ctime()} - {message}\n".format())
        f.close()




