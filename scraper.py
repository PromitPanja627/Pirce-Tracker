import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/AKG-K72-Close-Back-Studio-Headphones/dp/B01AYSNHVQ/ref=sr_1_1_sspa?crid=3AIYWUAMJQ4S&dchild=1&keywords=akg+k72&qid=1601905844&sprefix=akg+k%2Caps%2C288&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVdLSDdMM1k4M1hBJmVuY3J5cHRlZElkPUEwNzA1MTk0MjQ4MDc5REJaRDFJRSZlbmNyeXB0ZWRBZElkPUEwMTA5MTUxM0tPUjVHWlYyV1NWWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[2:7].replace(',', ''))

    if (converted_price < 2000) :
        send_mail()
    

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('promitpanja627@gmail.com', 'xjfdlwycyrxfvewp')

    subject = 'Price fell down!'
    body = 'check the amazon link https://www.amazon.in/AKG-K72-Close-Back-Studio-Headphones/dp/B01AYSNHVQ/ref=sr_1_1_sspa?crid=3AIYWUAMJQ4S&dchild=1&keywords=akg+k72&qid=1601905844&sprefix=akg+k%2Caps%2C288&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRVdLSDdMM1k4M1hBJmVuY3J5cHRlZElkPUEwNzA1MTk0MjQ4MDc5REJaRDFJRSZlbmNyeXB0ZWRBZElkPUEwMTA5MTUxM0tPUjVHWlYyV1NWWCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('promitpanja627@gmail.com', 'trashtom420@gmail.com', msg)
    print('HEY E-MAIL HAS BEEN SENT')

    server.quit()

    
while(True):
    check_price()
    time.sleep(86400)








    




