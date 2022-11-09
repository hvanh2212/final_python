import csv
from email import header
import bs4
import requests
import re
url = r'https://www.cisa.gov/uscert/ncas/alerts/2022'
re = requests.get(url)
soup = bs4.BeautifulSoup(re.text,'html.parser')
size = len(soup.select('.item-list li'))

string = soup.select('.item-list li')

soup_id = bs4.BeautifulSoup(str(string), 'html.parser')

listcontent=[]
listlink=[]
listdate=[]
listid=[]
listname=[]
for link in soup_id.find_all('span'):
    id_name = link.get_text()
    listid.append(id_name)
    listname.append(id_name[1])

    soup_link = bs4.BeautifulSoup(str(link), "html.parser")

    listlink.append('https://www.cisa.gov/uscert'+ soup_link.find("a", href = True)['href'])

for i in  listlink:
    request = requests.get(i)
    soup_date = bs4.BeautifulSoup(request.text,'html.parser')
    mydivs = soup_date.find_all('div',class_='submitted meta-text')
    
    listdate.append(str(mydivs).split('\n')[1].strip())

#write to csv . file
header = ['Alert ID','Alert Name','All Date','Link']
file_name='5a.csv'
with open(file_name, 'w', newline="") as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerow(header)
    for i in range(0, size):
        data=[listid[i],listname[i],listdate[i],listlink[i]]
        csvwriter.writerow(data)


##create and write data to excel
from openpyxl import Workbook
book = Workbook()
sheet = book.active
rows=(('Alert ID','Alert Name','All Date','Link'))
sheet.append(rows)
for i in range(0, size):
    data=[listid[i],listname[i],listdate[i],listlink[i]]
    sheet.append(data)
book.save('5b.xlsx')