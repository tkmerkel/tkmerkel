from sys import argv
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
import time
from twilio.rest import Client

# Twilio Account SID and Auth Token for sending Text Message
# Pass Twilio Keys Here
client = Client("###################", "#####################")

counter = 0

# counter is number of minutes to run, loops every minute
while counter < 120:
    print(counter)
    time.sleep(60)
    counter += 1
    # Load Recently Added Page From CoinGecko #
    url = 'https://www.coingecko.com/en/coins/recently_added'
    coin_page = requests.get(url)
    soup = BeautifulSoup(coin_page.content, 'html.parser')

    # Retrieve URL of first Coin
    tag = soup.find_all('td', class_="py-0 coin-name")[0]
    txt = str(tag)
    x = re.findall("href=\S*", txt)
    coin_url = x[0][6:-1]
    new_url = f'https://www.coingecko.com/{coin_url}'

    coin_page = requests.get(new_url)
    soup = BeautifulSoup(coin_page.content, 'html.parser')
    new_tag = soup.find_all('a', class_="coin-link-tag")

    # Collect Coin Info
    coin_links = []
    for link in new_tag:
        link = str(link)
        x = re.findall("href=\S*", link)
        #print(x[0][6:-1])
        coin_links.append(x[0][6:-1])

    f = open('coins.csv', 'r')
    lines = f.read().split(',')
    f.close()

    #Compare to see if Coin is same as last saved
    if lines[0] == coin_links[0]:
        print('No New Listing...')
        continue
    else:
        coins_file = open('coins.csv', 'w')
        message_body = 'NEW COIN LISTED ON COINGECKO!'
        for link in coin_links:
            coins_file.write(f'{link},\n')
            message_body += f' {link} '
        coins_file.close()

        # Send Text Message
        # Pass origin and destination numbers here
        client.messages.create(to="+11111111111",
                       from_="+12222222222",
                       body=message_body)

        print('!!! NEW COIN LISTED ON COINGECKO !!!!!')
        print('!!! NEW COIN LISTED ON COINGECKO !!!!!')
        print('!!! NEW COIN LISTED ON COINGECKO !!!!!')

        for links in coin_links:
            print(link)
