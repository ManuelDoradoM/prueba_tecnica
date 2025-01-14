from fastapi import APIRouter, HTTPException, responses
from datetime import date
from database_placeholder import data_base
from aux_functions.date_validation import date_validation
from aux_functions.booked_cars_by_date import booked_cars_by_date
from aux_functions.add_hiperlink import add_hiperlink
from aux_functions.del_books import del_books
from logger.utils.Logger import Logger

available_cars = APIRouter()

@available_cars.get('/available_cars')
def get_available_cars_by_date(date1: date = date.today(), date2: date = None):

    Logger.add_to_log('info', 'available_cars?date1={}&date2={}'.format(date1, date2))
    
    if date_validation(date1, date2):
        
        available_cars = list(filter(lambda car: not car['id'] in booked_cars_by_date(date1, date2), data_base.fleet))
        available_cars = [add_hiperlink(car, date1, date2) for car in available_cars]
        available_cars = [del_books(car) for car in available_cars]

        available_cars = responses.JSONResponse(available_cars)
        available_cars.headers['Cache-Control'] = 'no-cache'
        
        return available_cars
    
    Logger.add_to_log('warning', 'status_code = 400, "Fechas ingresadas invalidas."')
    raise HTTPException(
         status_code = 400,
         detail = 'Invalid dates.'
    )