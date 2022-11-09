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
    return read_file("email.csv")  

class email_info(BaseModel):
    email : str
    identifier : str
    first_name : str
    last_name : str

def create_obj(list):
    with open('email.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list)

@app.post("/")
async def create(info: email_info):
    list = [info.email, info.identifier, info.first_name, info.last_name]
    create_obj(list)
    return list

def find_index(email):
    # find index of row values is equal input
    csv_file = csv.reader(open('email.csv', "r"), delimiter=",")
    index = -1
    for row in csv_file:
        if email == row[0]:
            return index
        index += 1

def update_obj(list_input):
    # reading the csv file
    df = pd.read_csv("email.csv")

    index_row = find_index(list_input[0])
    df.loc[index_row, 'Identifier'] = list_input[1]
    df.loc[index_row, 'First name'] = list_input[2]
    df.loc[index_row, 'Last name'] = list_input[3]
    
    df.to_csv("email.csv", index=False)
    

@app.put("/")
async def update(info: email_info):
    list = [info.email, info.identifier, info.first_name, info.last_name]
    update_obj(list)
    return "update success"

class email_filter(BaseModel):
    email : str

def delete_obj(identifier):
    csv_file = csv.reader(open('email.csv', "r"), delimiter=",")
    list_email = []

    for row in csv_file:
        if identifier != row[0]:
            list_email.append(row)

    with open('email.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        for row in list_email:
            # write the data
            writer.writerow(row)


@app.delete("/")
def delete(email_input : email_filter):
    delete_obj(email_input.email)
    return "delete success"
