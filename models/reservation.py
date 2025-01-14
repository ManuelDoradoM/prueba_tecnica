from models.new_reservation import New_Reservation
from database_placeholder import data_base

class Reservation():

    def __init__(self, new_reservation: New_Reservation):

        self.id = data_base.total_reservation_length + 1
        data_base.total_reservation_length += 1
        self.usuario = new_reservation.usuario
        self.date_init = new_reservation.date_init
        self.date_finish = new_reservation.date_finish
        self.car_id = new_reservation.car_id