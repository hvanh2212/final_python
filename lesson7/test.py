import csv 
import json 

def csv_to_json(file):
    jsonArray = []
      
    #read csv file
    with open(file, encoding='utf-8') as f: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(f) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String
    return json.dumps(jsonArray)
          
file = r'file.csv'
print(csv_to_json(file))
