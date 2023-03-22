"""
Test whether the webhook server works
"""

from flask import Flask, request, abort
from discord import Webhook
import aiohttp
import asyncio

app = Flask(__name__)

# This is the discord webhook url
URL = ""


async def send_message():
    async with aiohttp.ClientSession() as session:
        wh = Webhook.from_url(URL, session=session)
        await wh.send('Hello World From the Internet', username='Test')


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        try:
            asyncio.run(send_message())
            return 'success', 200
        except Exception as E:
            print(E)
            print("failed")
    else:
        abort(400)


if __name__ == '__main__':
    app.run(port=9080)
