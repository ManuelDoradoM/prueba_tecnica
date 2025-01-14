from fastapi import FastAPI
from database_placeholder import data_base
from routers.get_available_cars import available_cars
from routers.post_reservation_car import booking

app = FastAPI()

@app.get('/fleet')
def get_fleet():
    return data_base.reservations

app.include_router(available_cars)
app.include_router(booking)