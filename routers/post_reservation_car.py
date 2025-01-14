from fastapi import APIRouter, HTTPException, responses
from database_placeholder import data_base
from models.new_reservation import New_Reservation
from models.reservation import Reservation
from aux_functions.date_validation import date_validation
from aux_functions.booked_date_by_car import booked_date_by_car
from aux_functions.booking import booking_car
from logger.utils.Logger import Logger

booking = APIRouter()

@booking.post('/booking')
def post_booking(reservation: New_Reservation):

    Logger.add_to_log('info', 'Reserva: {}'.format(str(reservation)))

    if date_validation(reservation.date_init, reservation.date_finish) and booked_date_by_car(reservation.car_id, reservation.date_init, reservation.date_finish):
        
        res = booking_car(reservation)
        reservas = responses.JSONResponse({'id': res.id, 'user': res.user, 'date_init': res.date_init.strftime('%Y,%m,%d'), 'date_finish': res.date_finish.strftime('%Y,%m,%d'), 'car_id': res.car_id})
        reservas.headers['Cache-Control'] = 'no-cache'
        return reservas

    else:
        Logger.add_to_log('warning', 'status_code = 400, "Fechas ingresadas invalidas."')
        raise HTTPException(
            status_code = 400,
            detail = 'Invalid dates.'
        )