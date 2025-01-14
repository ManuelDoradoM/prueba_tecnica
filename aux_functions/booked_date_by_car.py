from fastapi import HTTPException
from datetime import date
from database_placeholder import data_base

def booked_date_by_car(car_id: str, date1: date, date2: date):

    reservation_ids = None

    for car in data_base.fleet:
        if car['id'] == car_id:
            reservation_ids = car['books']
    
    if reservation_ids == None:
        raise HTTPException(
            status_code = 400,
            detail = 'The car id does not match an existing car.'
        )

    for res in data_base.reservations:
        if res.id in reservation_ids:
            if res.date_finish >= date1 and date2 >= res.date_init:
                raise HTTPException(
                    status_code = 400,
                    detail = 'The car is not available on the indicated date.'
                )
    
    return True