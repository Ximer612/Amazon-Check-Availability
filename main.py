import schedule
import telegram
import amazon

AMAZON_PRODUCT_LINK = input("Enter product link: ")
TELEGRAM_BOT_TOKEN = 'your-telegram-bot-token-here'
TELEGRAM_USER_NAME = 'your-telegram-user-name'

BOT_CHATID = telegram.get_bot_chatID(TELEGRAM_USER_NAME,TELEGRAM_BOT_TOKEN)

schedule.every(60).minutes.do(amazon.check,AMAZON_PRODUCT_LINK,TELEGRAM_BOT_TOKEN,BOT_CHATID)

print("Started checking!")
amazon.check(AMAZON_PRODUCT_LINK,TELEGRAM_BOT_TOKEN,BOT_CHATID)

while True:
    # running all pending tasks/jobs
    schedule.run_pending()
