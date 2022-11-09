from fastapi import FastAPI
import json
import csv
import pandas as pd
from pydantic import BaseModel


def read_file(file):
    json_list = []
      
    #read csv file
    with open(file, encoding='utf-8') as f: 
        csvReader = csv.DictReader(f) 

        #convert each csv row into dict
        for row in csvReader: 
            #add this dict to json array
            json_list.append(row)
  
    #convert python jsonArray to JSON String
    json_string = json.dumps(json_list)
    return json.loads(json_string)

app = FastAPI()

@app.get("/")
async def read():
    return read_file("file.csv")  

class object(BaseModel):
    identifier : str
    first_name : str
    last_name : str

def create_obj(list_input):
    with open('file.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(list_input)

@app.post("/")
async def create(obj: object):
    list_input = [obj.identifier, obj.first_name, obj.last_name]
    create_obj(list_input)
    return list_input

def find_row(identifier):
    # find index of row values is equal input
    csv_file = csv.reader(open('file.csv', "r"), delimiter=",")
    index = -1
    #loop through the csv list
    for row in csv_file:
        #if current row identifier is equal to input, return thw index
        if identifier == row[0]:
            return index
        index += 1

def update_obj(list_input):
    # reading the csv file
    df = pd.read_csv("file.csv")

    index_row = find_row(list_input[0])
    # updating the column value/data
    df.loc[index_row, 'First name'] = list_input[1]
    df.loc[index_row, 'Last name'] = list_input[2]
    
    # writing into the file
    df.to_csv("file.csv", index=False)
    

@app.put("/")
async def update(obj: object):
    """
    update object by identifier
    """
    list_input = [obj.identifier, obj.first_name, obj.last_name]
    update_obj(list_input)
    return "Success"

class identifier_values(BaseModel):
    identifier : str

def delete_obj(identifier):
    # find index of row values is e
    csv_file = csv.reader(open('file.csv', "r"), delimiter=",")
    list_obj = []

    #loop through the csv list
    for row in csv_file:
        #if current row identifier is equal to input, return thw index
        if identifier != row[0]:
            list_obj.append(row)

    with open('file.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for row in list_obj:
            # write the data
            writer.writerow(row)


@app.delete("/")
def delete(identifier_input : identifier_values):
    """
    delete object by identifier
    """
    delete_obj(identifier_input.identifier)
    return "Success"

