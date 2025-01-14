from fastapi import FastAPI
from database_placeholder import data_base

app = FastAPI()

@app.get('/fleet')
def get_fleet():
    return data_base.reservations
