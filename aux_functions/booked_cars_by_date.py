from datetime import date
from database_placeholder import data_base

def booked_cars_by_date(date1: date, date2: date = None):
    date2 = date1 if date2 == None else date2
    list_booked_cars = []
    for res in data_base.reservations:
        if res.date_finish >= date1 and date2 >= res.date_init:
                list_booked_cars.append(res.car_id)
    
    return list_booked_cars