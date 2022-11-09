import pandas as pd
import os
import re
import csv, yaml
import pandas as pd

"""
convert all file csv in folder to file yaml and json
"""

reg_json = re.compile(r'[.csv]$')


def csv_to_json(file):
    """
    convert file csv to file json
    """
    pdObj = pd.read_csv(folder +"/"+file)
    pdObj.to_json(folder + "/" + file[:-4]+'.json')

def csv_to_yaml(file):
    """
    convert file csv to file yaml
    """
    csv_data = []
    with open(folder +"/"+file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_data.append(row)
    
    with open(folder + "/" + file[:-4]+'.yaml', 'w') as outfile:
        outfile.write(yaml.dump(csv_data))

# input folder
folder = input("folder: ")

for i in os.listdir(folder):
    if re.search(reg_json, i):
        csv_to_json(i)
        csv_to_yaml(i)

print("Success")
