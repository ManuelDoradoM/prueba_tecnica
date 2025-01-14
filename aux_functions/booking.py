from models.reservation import Reservation
from database_placeholder import data_base


def booking_car(reservation: Reservation):

    res = Reservation(reservation)

    data_base.reservations.append(res)
    id_car = reservation.car_id

    for car in data_base.fleet:
        if car['id'] == id_car:
            car['books'].append(res.id)
            break

    return res
    