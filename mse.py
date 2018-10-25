# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_adu():

	page = requests.get("http://mse.mn/mn/company/231")
	soup = BeautifulSoup(page.content, 'html.parser')
	c = soup.find('div', class_='col-lg-6 col-md-6')
	c_a = soup.find_all('b')
	return 'APU:' + str(c_a[2].get_text()) + '₮'

print(get_adu())
