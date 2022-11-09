import os
import re
import pandas as pd
tester = re.compile(r"[.json]$") #to compile into a re.pattern and use to search for a match inside different target strings
for i in os.listdir('folder'): #returns a list containing the names of the entries in the directory given by path
    if re.search(tester, i): #search "}" in all files
        pdObj = pd.read_json('folder/'+i)
        pdObj.to_csv('folder/'+i[:-5]+".csv")