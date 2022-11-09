import pandas as pd
import os
import re
import csv

"""
convert all file csv in folder to file csv
"""

reg_json = re.compile(r'[.json]$')


def json_to_csv(file):
    """
    convert file json to csv
    """
    pdObj = pd.read_json(folder +"/"+file, orient='index')
    pdObj.to_csv(folder + "/" + file[:-5]+'.csv', index=False)


folder = input("folder: ")

for i in os.listdir(folder):
    if re.search(reg_json, i):
        json_to_csv(i)

print("Success")
