from fastapi import FastAPI
from sql_management import CURD_function
from pydantic import BaseModel
from typing import Union

class Ticket_input(BaseModel):
    ticket_name : str
    ticket_description : str
    status_name : str
    assignee_id : str
    assigneer_id : str
    category_name : str
    priority_name : str


app = FastAPI()

@app.get("/owner")
async def owner():
    """
    list all owner
    """
    return CURD_function.select_owner()

@app.get("/ticket")
async def ticket():
    """
    list all ticket
    """
    return CURD_function.select_ticket()

@app.post("/ticket")
async def create_ticket(ticket: Ticket_input):
    """
    create ticket
    """
    return CURD_function.create_ticket(ticket)

class filter_ticket(BaseModel):
    filter_values: str

@app.post("/ticket_filte_by_category/{category_name}")
async def ticket_filter_by_category(ticket_filter_category: filter_ticket):
    """
    list all tickets which has category_name equal to input string
    """
    return CURD_function.filter_ticket_by_category(ticket_filter_category.filter_values)


@app.post("/ticket_filter_by_name/{ticket_name}")
async def ticket_filter_by_name(ticket_name_filter: filter_ticket):
    """
    list all tickets which ticket_name contain an input string
    """
    return CURD_function.filter_ticket(ticket_name_filter.filter_values)


@app.post("/ticket_filter_by_owner/{owner_name}") 
async def ticket_filter_by_owner(ticket_owner_filter: filter_ticket):
    """
    list all tickets which belong to this owner_name or owner_mail
    """
    return CURD_function.filter_ticket_owner(ticket_owner_filter.filter_values)

class Ticket_update(Ticket_input):
    ticket_id : str

@app.put("/ticket/{ticket_id}")
async def update_ticket(ticket: Ticket_update):
    """
    Update ticket details (change ticket info except ticket_id, and re-update the updated_time)
    """
    return CURD_function.update_ticket(ticket)

class delete_ticket(BaseModel):
    tickets_id: list

@app.delete("/ticket/{ticket_id}")
async def delete_ticket_by_id(ticket_filter: delete_ticket):
    """
    Delete a ticket by ID. Can delete multiple tickets at once if user pass a list to API. Ex: {“ticket_ids”: [“1”, “2”, “3”]}
    """
    return CURD_function.delete_ticket(ticket_filter.tickets_id)
