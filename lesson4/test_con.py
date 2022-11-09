import requests
from lxml import html
url = 'https://www.cisa.gov/uscert/ncas/alerts'
doc = html.fromstring(requests.get(url).text)
print("The number of security alerts issued by US-CERT in the current year:")
print(doc.cssselect('.item-list li'))
print(len(doc.cssselect('.item-list li')))