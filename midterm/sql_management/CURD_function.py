from unicodedata import category
from sqlalchemy import Column, String, ForeignKey, DateTime, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json
import uuid

Base = declarative_base()

class Owner(Base):
    __tablename__ = 'owner'
    owner_id = Column(String, primary_key=True, autoincrement=True)
    owner_name = Column(String, nullable = False)
    owner_mail = Column(String, nullable = False)

    def dict(self):
        return{
            "owner_id" : self.owner_id,
            "owner_name" : self.owner_name,
            "owner_mail" : self.owner_mail
        }

class Ticket(Base):
    __tablename__ = 'tickets'
    ticket_id = Column(String, primary_key=True, autoincrement=True)
    ticket_name = Column(String, nullable = False)
    ticket_description = Column(String, nullable = False)
    created_time = Column(String, default = str(datetime.now()))
    update_time = Column(String, default = str(datetime.now()))
    status_name = Column(String)
    assignee_id = Column(String, ForeignKey('owner.owner_id'))
    assigneer_id = Column(String, ForeignKey('owner.owner_id'))
    category_name = Column(String, nullable = False)
    priority_name = Column(String)

    def dict(self):
        return{
            "ticket_id" : self.ticket_id,
            "ticket_name" : self.ticket_name,
            "ticket_description" : self.ticket_description,
            "created_time" : self.created_time,
            "update_time" : self.update_time,
            "status_name" : self.status_name,
            "assignee_id" : self.assignee_id,
            "assigneer_id" : self.assigneer_id,
            "category_name" : self.category_name,
            "priority_name" : self.priority_name
        }


def create_session():
    engine = create_engine('sqlite:///./models/ticket_system.db')
    # create session
    Session = sessionmaker(bind=engine)
    return Session()

def json_output(tickets):
    """
    return Json
    """
    list_dict = []
    
    # add dict to the list
    for ticket in tickets:
        list_dict.append(dict(ticket.dict()))
    # convert a list to json
    string_json = json.dumps(list_dict)

    # parse a valid JSON string and convert it to dict
    return json.loads(string_json) 


def create_ticket(ticket_json):
    """
    create ticket
    """
    session = create_session()

    ticket_created = Ticket(ticket_id = str(uuid.uuid4()),
                            ticket_name = ticket_json.ticket_name,
                            ticket_description = ticket_json.ticket_description,
                            update_time = "",
                            status_name = ticket_json.status_name,
                            assignee_id = ticket_json.assignee_id,
                            assigneer_id = ticket_json.assigneer_id,
                            category_name = ticket_json.category_name,
                            priority_name = ticket_json.priority_name)

    session.add(ticket_created)
    session.commit()
    string_json = json.dumps(ticket_created.dict())
    return json.loads(string_json) 

def select_owner():
    """
    select all owner
    """
    session = create_session()
    # SELECT * FROM Customers;
    owners = session.query(Owner).all()

    list_dict = []
    
    # add dict to the list
    for owner in owners:
        list_dict.append(dict(owner.dict()))
    # convert a list to json
    string_json = json.dumps(list_dict)

    # parse a valid JSON string and convert it to dict
    return json.loads(string_json) 

def select_ticket():
    """
    select all ticket
    """
    session = create_session()
    # SELECT * FROM Customers;
    tickets = session.query(Ticket).all()

    return json_output(tickets)


def filter_ticket(ticket_name_filter):
    """
    list all tickets which ticket_name contain an input string
    """
    session = create_session()
    tickets = session.query(Ticket).filter(Ticket.ticket_name.contains(ticket_name_filter)).all()
    
    return json_output(tickets)

def filter_ticket_by_category(category_filter):
    """
    list all tickets which has category_name equal to input string
    """
    session = create_session()
    tickets = session.query(Ticket).filter(Ticket.category_name == category_filter).all()

    return json_output(tickets)

def filter_ticket_owner(owner_filter):
    """
    list all tickets which belong to this owner_name or owner_mail
    """
    session = create_session()

    list_ticket = []

    for tickets, i in session.query(Ticket, Owner).filter(Ticket.assignee_id == Owner.owner_id,or_(Owner.owner_mail == owner_filter,  Owner.owner_name == owner_filter)).all():
        ticket= Ticket(ticket_id = tickets.ticket_id,
                        ticket_name = tickets.ticket_name,
                        ticket_description = tickets.ticket_description,
                        created_time = tickets.created_time,
                        update_time = tickets.update_time,
                        status_name = tickets.status_name,
                        assignee_id = tickets.assignee_id,
                        assigneer_id = tickets.assigneer_id,
                        category_name = tickets.category_name,
                        priority_name = tickets.priority_name)
        list_ticket.append(ticket)

    return json_output(list_ticket)


def delete_ticket(tickets_id):
    """
    Delete a ticket by ID. Can delete multiple tickets at once if user pass a list to API. 
    Ex: {“ticket_ids”: [“1”, “2”, “3”]}
    a django project is a collection configurations and application that together make up a given
    it includes default implementations
    """
    session = create_session()
    # filter the customer has ticket_id 
    list_dict = []
    for ticket_id_filter in tickets_id:
        ticket = session.query(Ticket).filter(Ticket.ticket_id == ticket_id_filter).first()
        list_dict.append(dict(ticket.dict()))
        #delete the customer 
        session.delete(ticket)
        session.commit()
    string_json = json.dumps(list_dict)
    return json.loads(string_json) 

def update_ticket(ticket_json):
    """
    Update ticket details (change ticket info except ticket_id, and re-update the updated_time)
    a custoe with of 10 items and maximium of 1000 istem
    casc container omage trong mot project 
    
    """
    session = create_session()

    ticket = session.query(Ticket).filter(Ticket.ticket_id == ticket_json.ticket_id).first()

    ticket.ticket_name = ticket_json.ticket_name
    ticket.ticket_description = ticket_json.ticket_description
    ticket.update_time = str(datetime.now())
    ticket.status_name = ticket_json.status_name
    ticket.assignee_id = ticket_json.assignee_id
    ticket.assigneer_id = ticket_json.assigneer_id
    ticket.category_name = ticket_json.category_name
    ticket.priority_name = ticket_json.priority_name

    session.commit()
    string_json = json.dumps(ticket.dict())
    return json.loads(string_json) 