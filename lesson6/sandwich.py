import pyinputplus as pyip
from sqlalchemy import Column, String, ForeignKey, DateTime, or_, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid


Base = declarative_base()

class orders(Base):
    __tablename__ = 'orders'
    id = Column(String, primary_key=True)
    bread = Column(String)
    protein = Column(String)
    cheese = Column(String)
    cheese_type = Column(String)
    mayo = Column(String )
    mustard = Column(String )
    lettuce = Column(String )
    tomato = Column(String )
    amount = Column(Integer )
    total_cost = Column(Integer )

class prices(Base):
    __tablename__ = 'prices'
    name = Column(String, primary_key=True)
    prices = Column(Integer)


engine = create_engine('sqlite:///./lesson6.db')
    # create session
Session = sessionmaker(bind=engine)
session = Session()
prices_list = session.query(prices).all()

total_cost_in = 0

def cost(name):
    for i in prices_list:
        if i.prices == name:
            return i.prices

print("bread: ")
bread_in = pyip.inputMenu(["wheat", "white", "sourdough"])
total_cost_in += cost(bread_in)

print("protein: ")
protein_in = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
total_cost_in += cost(protein_in)

cheese_in = pyip.inputYesNo('cheese? (y or n): ')
if cheese_in == 'yes':
    cheese_type_in = pyip.inputMenu(['cheddar','swiss','mozzarella'])
    total_cost_in += cost(cheese_type_in)
else:
    cheese_type_in = ""

mayo_in = pyip.inputYesNo('mayo? (y or n): ')
if mayo_in == 'yes':
    total_cost_in += cost('mayo')

mustard_in = pyip.inputYesNo('mustard? (y or n): ')
if mustard_in == 'yes':
    total_cost_in += cost('mustard')

lettuce_in = pyip.inputYesNo('lettuce? (y or n): ')
if lettuce_in == 'yes':
    total_cost_in += cost('lettuce')

tomato_in = pyip.inputYesNo('tomato? (y or n): ')
if tomato_in == 'yes':
    total_cost_in += cost('tomato')

amount_in = pyip.inputInt('amount: ')
total_cost_in = total_cost_in * amount_in

order = orders(id = str(uuid.uuid4()),
               bread = bread_in,
               protein = protein_in,
               cheese = cheese_in,
               cheese_type = cheese_type_in,
               mayo = mayo_in,
               mustard = mustard_in,
               lettuce = lettuce_in,
               tomato = tomato_in,
               amount = amount_in,
               total_cost = total_cost_in)


session.add(order)
session.commit()
print('total cost: '+ str(total_cost_in))




