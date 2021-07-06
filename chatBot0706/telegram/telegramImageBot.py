from flask import Flask, request

# pip install python-telegram-bot
# pip install telegram
import telegram
from credentials import bot_token, URL

TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# 텔레그램 봇과 url 연동 
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook(f'{URL}/{TOKEN}')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

# 실제로 텔레그램에서 request를 보내는 URL
# 텔레그램의 경우 <URL>/<TOKEN> 으로 http request 전송
@app.route(f'/{TOKEN}', methods=['POST'])
def autoResponse():
	# request를 json 형식으로 받은 다음 Telegram object로 변환
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id # request를 발생시킨 채팅방의 id
    msg_id = update.message.message_id # request를 발생시킨 메시지의 id

    # 유저가 보낸 메시지 읽기 (텔레그램은 utf-8를 사용하기에 서버에서 사용하는 unicode와 호환을 위해 utf-8으로 인코딩을 한 후 디코드)
    text = update.message.text.encode('utf-8').decode()
    #resp = request.get_json(force=True)

    try:
        # 유저가 보낸 메시지에 대한 답장으로 유저 메시지 반복하기
        if text.replace(" ", "") == '박서준':
            bot.sendMessage(chat_id=chat_id, text="박서준입니다.")
        elif text.replace(" ", "") == '강아지' or text.replace(" ", "") == '개':
            bot.sendMessage(chat_id=chat_id, text="멍멍")
        else:
            bot.sendMessage(chat_id=chat_id, text=text)
    except Exception:
        # 에러가 발생했을 때
        bot.sendMessage(chat_id=chat_id, text="문제가 발생하였습니다 :(")
    try:
        #이미지 보내기
        if text.replace(" ", "") == '박서준':
            bot.send_photo(chat_id=chat_id, photo='https://search.pstatic.net/common?type=a&size=120x150&quality=95&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2Fportrait%2F202003%2F20200310125523968.jpg')
        elif text.replace(" ", "") == '강아지' or text.replace(" ", "") == '개':
            bot.send_photo(chat_id=chat_id, photo='https://mblogthumb-phinf.pstatic.net/MjAxOTEwMjJfMTE5/MDAxNTcxNzI5OTEwNzU5.OaHDR8EYE87YvZRaM4WIADp3chZOPRy_dymAVxgGiJUg.lrfhLGExijfM8e9uhOKrL32XND8GLYOg0GQ9T3NMFgAg.JPEG.animalandhuman/IMG_8805.JPG?type=w800')
        else:
            bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
    except Exception:
    	# 에러가 발생했을 때
    	bot.sendMessage(chat_id=chat_id, text="문제가 발생하였습니다 :(", reply_to_message_id=msg_id)

    return "ok"

    # try:
    # 	# 이미지 보내기 https://telegram.org/img/t_logo.png
    #     bot.send_photo(chat_id=chat_id, photo='https://search.pstatic.net/common?type=a&size=120x150&quality=95&direct=true&src=http%3A%2F%2Fsstatic.naver.net%2Fpeople%2Fportrait%2F202003%2F20200310125523968.jpg')
    # except Exception:
    # 	# 에러가 발생했을 때
    # 	bot.sendMessage(chat_id=chat_id, text="문제가 발생하였습니다 :(", reply_to_message_id=msg_id)
    #
    # return "ok"

if __name__ == '__main__':
	app.run(debug=True)
