from bs4 import BeautifulSoup
import requests
import numpy as np

page = requests.get('https://www.zaubacorp.com/company/BUSINESSONBOT-PRIVATE-LIMITED/U72900KA2020PTC136387')
soup = BeautifulSoup(page.content, 'html.parser')

alls = []
for d in soup.findAll('div', attrs={'class':'contaier'}):
    #print(d)
    n = d.find('div', attrs={'class':'container information'})
    content =n.find_all('br')
    print(content[0])