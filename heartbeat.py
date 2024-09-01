import time
import os
import requests

# Get the heartbeat ID from the environment variable
heartbeat_id = os.getenv("HEARTBEAT_ID")
url = f"https://uptime.betterstack.com/api/v1/heartbeat/{heartbeat_id}"

while True:
    try:
        response = requests.get(url)
        print(f"Heartbeat sent. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(1800)  # Wait for 30 minutes (1800 seconds) before sending the next request
