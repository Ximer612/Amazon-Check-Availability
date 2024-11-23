from telegram import bot_send_text
import bs4
import requests

def check(AMAZON_PRODUCT_LINK,BOT_TOKEN,BOT_CHATID):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    res = requests.get(AMAZON_PRODUCT_LINK,headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup_item_name = soup.find('span', id='productTitle')
    soup_seller_name = soup.find('a', id='sellerProfileTriggerId')

    seller_name = str(soup_seller_name)
    item_name = str(soup_item_name.contents[0]).strip()

    if  seller_name == 'None' or seller_name is None or seller_name == 'Amazon':
        bot_send_text(item_name+" is now sold by amazon!",BOT_TOKEN,BOT_CHATID)
        print("\x1b[42m"+ item_name+" is now sold by amazon!"+ "\x1b[0m")
    else:
        print("\x1b[41m"+item_name+" is sold by "+soup_seller_name.next+ "!\x1b[0m")