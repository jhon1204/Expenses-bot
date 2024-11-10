import requests
import os

TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}"
response = requests.get(url)

if response.status_code == 200:
    print("Webhook set successfully")
else:
    print("Failed to set webhook")