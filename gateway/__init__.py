from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.environ["BASE_URL"]
TOKEN = os.environ["TOKEN"]
PRIORITY = int(os.environ["PRIORITY"])
VERIFY_SSL = os.environ["VERIFY_SSL"].lower() == "true"

app = Flask(__name__)


@app.route('/push', methods=["POST"])
def push():
    data = request.json
    title = data["commonAnnotations"]["summary"]
    description = data["commonAnnotations"]["description"]

    message = f"{data['status']} - {description}"

    requests.post(
        f"{BASE_URL}/message?token={TOKEN}",
        {"title": title, "message": message, "priority": PRIORITY},
        verify=VERIFY_SSL
    )

    return "ok"
