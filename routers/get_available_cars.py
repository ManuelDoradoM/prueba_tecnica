from fastapi import APIRouter, HTTPException, responses
from datetime import date
from database_placeholder import data_base

available_cars = APIRouter()

@available_cars.get('/available_cars')
def get_available_cars_by_date(date1: date = date.today(), date2: date = None):
    pass