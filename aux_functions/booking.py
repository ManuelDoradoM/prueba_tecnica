from models.reservation import Reservation
from database_placeholder import data_base
from logger.utils.Logger import Logger


def booking_car(reservation: Reservation):

    res = Reservation(reservation)

    data_base.reservations.append(res)
    id_car = reservation.car_id

    for car in data_base.fleet:
        if car['id'] == id_car:
            car['books'].append(res.id)
            break

    Logger.add_to_log('info', 'Reservation created: {}'.format(res.id))
    return res