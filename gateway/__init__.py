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

    for alert in data["alerts"]:

        title = alert["annotations"]["summary"]
        description = alert["annotations"]["description"]

        message = f"{alert['status']} - {description}"

        requests.post(
            f"{BASE_URL}/message?token={TOKEN}",
            {"title": title, "message": message, "priority": PRIORITY},
            verify=VERIFY_SSL
        )

    return "ok"
