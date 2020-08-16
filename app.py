from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
# 存取權
line_bot_api = LineBotApi(
    'cbFkKkjJUgLz66YXwkP7tn6tsbsUlXMunvVtblp0218GhqPufddy+oWaW8X9xcsnb54ATXV39LTaa1PJ6FUYEKHSbkwXx4lV3tUwJt3zDSRYjSkLPPabxAwJc6ocMxBcetpGcxR7HOJXoBvNNJbjzwdB04t89/1O/w1cDnyilFU=')
# 密碼
handler = WebhookHandler('d3c76e6b651eb353be9a8d9e632acba3')

# 接收line傳來的信息


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
