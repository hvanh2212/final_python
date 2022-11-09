import re
import requests
from bs4 import BeautifulSoup

site = "https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales"

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')


urls = [img['src'] for img in img_tags]

for url in urls:
    print((url))
    # filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    # if not filename:
    #      print("Regex didn't match with the url: {}".format(url))
    #      continue
    # with open("/home/ubuntu/fa_folder/lesson4/dowload_img/unit3.txt", 'wb') as f:
    #     if 'http' not in url:
    #         # sometimes an image source can be relative 
    #         # if it is provide the base url which also happens 
    #         # to be the site variable atm. 
    #         url = '{}{}'.format(site, url)
    #     response = requests.get(url)
    #     f.write(response.content)