"""
TRELLO-CORD WEBHOOK

Written for UNSW PCSoc

This is the webhook server, it receives updates from the trello board and sends messages in the chat
Where to send the message is specified the webhook url found in the webhook section of the integrations in Discord
"""

from flask import Flask, request, abort
import asyncio
from discord import Webhook
import aiohttp

# This is the url of the discord webhook
URL = ""


async def send_message():
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(URL, session=session)
        await webhook.send('The Trello Board has been updated', username='TrelloBot')


# async def bar():
#     await foo()

app = Flask(__name__)


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
    app.run()