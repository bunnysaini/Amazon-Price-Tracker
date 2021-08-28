import requests
from bs4 import BeautifulSoup
from mail import NotificationManager

notification = NotificationManager()
DESIRED_PRICE = 370.00                              # Add Your Desired Price for the Product
url = "https://www.amazon.in/Product"               # Add Product URL
recipient = "testemail@gmail.com"                   # Add Email ID
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url, headers=headers)
response.raise_for_status()
amazon = response.text

soup = BeautifulSoup(amazon, "html.parser")
name = soup.find(name="span", id="productTitle").getText()
price = float(soup.find(name="span", class_="a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P").getText().split("₹")[1])

if price < DESIRED_PRICE:
    body = f'{name} is available <b>only at ₹{price}</b>, Hurry and place your order now! <br><a href={url}> Click here! </a>'
    notification.send_mail(recipient, body)
