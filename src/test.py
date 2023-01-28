"""
Test whether pcsoc server is compatible with trello webhook api
"""

from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # print(request.json)
        try:
            print("the webhook is working")
            return 'success', 200
        except Exception as E:
            print(E)
            print("failed")
    else:
        abort(400)

if __name__ == '__main__':
    app.run()



