import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(
    message: str,
    token=os.getenv("TELEGRAM_TOKEM"), 
    chat_id=os.getenv("CHAT_ID")
  ):
  url = f"https://api.telegram.org/bot{token}/sendMessage"
  payload = {
    "chat_id": chat_id,
    "text": message
  }
  requests.post(url, json=payload)

# send_telegram_message(token, chat_id, message)