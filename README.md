## Shipping via Amazon checker
A simple python script to check if an Amazon product is being sold by Amazon itself and send a Telegram message when it is.
## How to run it?
Before install all requirements to run this program by doing:
```python
pip install requirements.txt
```
Next set telegram all variables to yours: TELEGRAM_BOT_TOKEN, TELEGRAM_USER_NAME

Next run it by doing:
```python
python main.py
```
And when asked "Enter product link:" paste the url of the product in the console and press Enter.

Now just wait for the notification to be sent! :)

## Known issues:
- May crash if the product has multiple "styles" like clothings