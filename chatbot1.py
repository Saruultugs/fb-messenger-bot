# -*- coding: utf-8 -*-
import requests
import json
import urllib
import datetime

end = datetime.date.today()
hansh = "http://monxansh.appspot.com/xansh.json?currency=USD"
resp = requests.get(hansh).json()
if resp != []:
    price = resp[0]['rate_float']
    name = resp[0]['name']
    mnt = price
else:
    mnt = 2000

def number(num):
    if num < 0.01:
        return str('%.8f' % num)
    else:
        num = '{:,.2f}'.format(num)
	return num
def change(num):
    if num < 0:
        return str(num) 
    else:
        return str('+'+ str(num))
    
def get_p(message_text):
    text = message_text.upper()
    if message_text == 'ONECOIN':
	return 'Ичээч'
    if message_text == 'UUU':
	return 'LOL'
    #text = message_text.upper()
	text = message_text.lower()

    listing = 'https://api.coinmarketcap.com/v2/listings/'
    getlist = requests.get(listing).json()
    b = getlist['data']
    try:
        for i in b:
            text = message_text.title()
            if i['name'] == text:
                a = i['id']
            else:
                text = text.upper()
                if i['symbol'] == text:
                    a = i['id']
                    
        url = 'https://api.coinmarketcap.com/v2/ticker/{}/?convert=BTC'
        tick = requests.get(url.format(a)).json()

        if tick != []:
            #url = 'https://api.coinmarketcap.com/v2/ticker/{}/?convert=BTC'.format(a)
            #tick = requests.get(url).json()
            c = tick['data']
            name = tick['data']['name']
            symbol = tick['data']['symbol']
            rank = tick['data']['rank']
            circulating_supply = tick['data']['circulating_supply']
            total_supply = tick['data']['total_supply']
            max_supply = tick['data']['max_supply']
            ###############  USD #########################################
            usd = tick['data']['quotes']['USD']['price']
            u_volume_24h = tick['data']['quotes']['USD']['volume_24h']
            u_market_cap = tick['data']['quotes']['USD']['market_cap']
            u_percent_change_1h = tick['data']['quotes']['USD']['percent_change_1h']
            u_percent_change_24h = tick['data']['quotes']['USD']['percent_change_24h']
            u_percent_change_7d = tick['data']['quotes']['USD']['percent_change_7d']

            btc = tick['data']['quotes']['BTC']['price']
            volume_24h = tick['data']['quotes']['BTC']['volume_24h']
            market_cap = tick['data']['quotes']['BTC']['market_cap']
            percent_change_1h = tick['data']['quotes']['BTC']['percent_change_1h']
            percent_change_24h = tick['data']['quotes']['BTC']['percent_change_24h']
            percent_change_7d = tick['data']['quotes']['BTC']['percent_change_7d']

            etherul = 'https://api.coinmarketcap.com/v2/ticker/{}/?convert=ETH'.format(a)
            ether = requests.get(etherul).json()
            d = ether['data']

            eth = ether['data']['quotes']['ETH']['price']
            volume_24h = ether['data']['quotes']['ETH']['volume_24h']
            market_cap = ether['data']['quotes']['ETH']['market_cap']
            percent_change_1h = ether['data']['quotes']['ETH']['percent_change_1h']
            percent_change_24h = ether['data']['quotes']['ETH']['percent_change_24h']
            percent_change_7d = ether['data']['quotes']['ETH']['percent_change_7d']

            #mnt = 2567
        brief = '*usd:* ' + '{}'.format(number(usd)) + '\n' + '*btc:* ' + '{}'.format(number(btc)) + '\n' + '*eth:* ' + '{}'.format(number(eth)) + '\n' + '*төг:* ' + '{}'.format(number(usd*mnt))+ ' ₮'  + '\n'  + '*24 цагт:* ' + '{}'.format(change(u_percent_change_24h)) + '%'
        return brief
            
    except:
        r = text.upper()
	r = r.encode('utf-8')
        hansh = "http://monxansh.appspot.com/xansh.json?currency={}"
        response = requests.get(hansh.format(r)).json()
        if response != []:
            price = response[0]['rate_float']
            name = response[0]['name']
	    namee = name.encode('utf-8')
            st = '{}: '.format(namee) + str(price) + ' ₮'
            return st
        else:
            return 'Тийм зоос байдаг юм уу? '
        #else:
            #return 'Kod Buruu'
#print(get_p('hoT'))
