import requests
from bs4 import BeautifulSoup as bs
import csv
from openpyxl import Workbook

"""
Write a Python program get alerts issued by US-CERT in the current year and write output to CSV and Excel file. 
Source: https://www.us-cert.gov/ncas/alerts

Output fields: Alert ID, Alert Name, Release Date, Last revised, Tips, Alert Link
"""

# url to get security alerts issued by US-CERT in the current year
url = 'https://www.cisa.gov/uscert/ncas/alerts/2022'
soup = bs(requests.get(url).content, "html.parser")

list_link = []

list_name = []

list_id = []

list_tips = []

list_date = []

list_revised = []

#find all <div class = "views-field views-field-title">
mydivs = soup.findAll("div", {"class": "views-field views-field-title"})
# number of security alerts issued by US-CERT in the current year
size = len(mydivs)

soup_id_name = bs(str(mydivs), "html.parser")

id_name = soup_id_name.find_all("span")
# get Alert ID, Alert Name, Alert Link
for i in id_name:
    list_id_name = i.get_text().split(":",maxsplit=1)
    list_id.append(list_id_name[0])
    list_name.append(list_id_name[1])

    soup_link = bs(str(i), "html.parser")

    list_link.append('https://www.cisa.gov/uscert'+soup_link.find("a", href = True)['href'])
# get Release Date, Last revised, Tips
for i in  list_link:
    soup_date_tip = bs(requests.get(i).content, "html.parser")
    date_list = soup_date_tip.find_all("div", {"class": "submitted meta-text"})
    for d in date_list:
        list_date_revised = d.get_text().strip().split("|")
        list_date.append(list_date_revised[0][23:])
        try:
            list_revised.append(list_date_revised[1][15:])
        except:
            list_revised.append("None")
    
    tip_list = soup_date_tip.find_all("p", {"class": "tip-intro"})
    for a in tip_list:
        list_tips.append((a.get_text()))

# write data to csv
header = ['Alert ID','Alert Name','Release Date', 'Last revised','Alert Link']
file_name = 'unit1.csv'
with open(file_name, 'w', newline="") as file:
    csvwriter = csv.writer(file) 
    csvwriter.writerow(header)
    for i in range(size):
        data = [list_id[i],list_name[i],list_date[i],list_revised[i], list_link[i]]
        csvwriter.writerow(data) 

# write data to excel
book = Workbook()
sheet = book.active
rows=('Alert ID','Alert Name','Release Date', 'Last revised','Alert Link')
sheet.append(rows)
for i in range(size):
    data = [list_id[i],list_name[i],list_date[i],list_revised[i], list_link[i]]
    sheet.append(data)
book.save('unit1.xlsx')   

