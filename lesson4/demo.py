from fastapi import FastAPI
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

"""
- Set up API using FASTApi
- Read Sample Database with SQLAlchemy
- Create function query all customer
- Create API path: /customer (GET)
"""

# create class Customer, mapping with table Customers
Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customers'
    CustomerId = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable = False)
    LastName = Column(String, nullable = False)
    Company = Column(String)
    Address = Column(String)
    City = Column(String)
    State = Column(String)
    Country = Column(String)
    PostalCode = Column(String)
    Phone = Column(String)
    Fax = Column(String)
    Email = Column(String)
    SupportRepId  = Column(Integer)

    def dict(self):
        return{
            "CustomerId" : self.CustomerId,
            "FirstName" : self.FirstName,
            "LastName" : self.LastName,
            "Company" : self.Company,
            "Address" : self.Address,
            "City" : self.City,
            "State" : self.State,
            "Country" : self.Country,
            "PostalCode" : self.PostalCode,
            "Phone" : self.Phone,
            "Fax" : self.Fax,
            "Email" : self.Email,
            "SupportRepId" : self.SupportRepId
        }

def create_session():
    engine = create_engine('sqlite:///./chinook.db')
    # create session
    Session = sessionmaker(bind=engine)
    return Session()

def select_customers():
    """
    select all customer from Customers
    """
    session = create_session()
    # SELECT * FROM Customers;
    customers = session.query(Customer).all()
    return customers


app = FastAPI()

@app.get("/customer")
async def customer():
    # list contains a list of dict
    # the dict is customer.dict()
    list_dict = []
    customers = select_customers()
    # add dict to the list
    for customer in customers:
        list_dict.append(dict(customer.dict()))
    # convert a list to json
    string_json = json.dumps(list_dict)

    # parse a valid JSON string and convert it to dict
    return json.loads(string_json)    

"""
- Set up API using FASTApi
- Read Sample Database with SQLAlchemy
- Create Delete function to delete
- Create API path: /customer (DELETE)
"""

def delete_customer():
    session = create_session()
    # filter the customer has CustomerId = 8
    customer = session.query(Customer).filter(Customer.CustomerId == 8).first()
    #delete the customer 
    session.delete(customer)
    session.commit()
    return customer.dict()

@app.delete("/customer")
async def customer():
    return delete_customer()  

@app.get("/")
async def root():
    return "Create API path: /customer (GET) and create API path: /customer (DELETE)"