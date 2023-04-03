import requests 
from bs4 import BeautifulSoup as soup 
import string
import re
ip = str(input("put target hosthere:>")).strip()
agents = list(string.ascii_uppercase)
for agent in agents:
	print(agent)
	headers = {
		'User-Agent' :f"{agent}"
	}
	res = requests.get(ip,headers=headers)
	bs_obj =soup(res.text,features="html.parser")
	text_e = bs_obj.get_text()
	text_e = re.sub("\s{1,1000}"," ",text_e)
	print(text_e)
