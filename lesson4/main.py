from typing import Union
import sqlalchemy as db
from fastapi import FastAPI
import json
engine = db.create_engine(r'sqlite:///chinook.db')
connection = engine.connect()
metadata = db.MetaData()
chinook = db.Table('customers', metadata, autoload=True, autoload_with=engine)
def query():
    query = db.select([chinook]) 
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    for i in range(len(ResultSet)):
        #print(check[i],end='\n\n') 
        c=dict(ResultSet[i])
        d=json.dumps(c)
    return d
'''def deletebyid(id):
   query = db.delete(customers)
   query = query.where(customers.columns.id =id)
   results = connection.execute(query)'''


app = FastAPI()


@app.get("/")
def read_root():
    return {'Hello': 'World'}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/customer")
def read_customers():
  return {'Hello': 'World'}
   
    