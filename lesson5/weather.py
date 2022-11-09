import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

API_KEY = '91ff1ebd0e844ded9cc41815220906'
days = 5

class ClassSchema(BaseModel):
    city: str
    country: str

@app.post('/forecast')
def get_forecast_5days(schema: ClassSchema):
    res = requests.get('https://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days={2}&country={3}&aqi=no&alerts=no'.format(
        API_KEY, 
        schema.city, 
        str(days), 
        schema.country))
    return res.text