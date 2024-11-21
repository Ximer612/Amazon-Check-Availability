import requests
import json

def get_bot_chatID(TELEGRAM_USER_NAME, BOT_TOKEN):
    if BOT_TOKEN == 'your-telegram-bot-token-here':
        exit("Please set your telegram bot token!")

    if TELEGRAM_USER_NAME == 'your-telegram-user-name':
        exit("Please set your telegram user name!")

    TELEGRAM_BOT_LINK = 'https://api.telegram.org/bot'+BOT_TOKEN+'/getUpdates'
    res = requests.get(TELEGRAM_BOT_LINK)
    res.raise_for_status()
    json_object = json.loads(res.content)

    for result in json_object['result']:
        result_user_name = result['message']['from']['username']

        if result_user_name == TELEGRAM_USER_NAME:
            id = result['message']['from']['id']
            return id
    
    exit("User name not found!")
    return None

def bot_send_text(bot_message,BOT_TOKEN,BOT_CHATID):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + \
        '/sendMessage?chat_id=' + str(BOT_CHATID) + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
