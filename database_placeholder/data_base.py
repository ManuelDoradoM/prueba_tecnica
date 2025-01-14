cars_model = [
    {
        'id': 0,
        'brand': 'brand1',
        'model': 'model1',
        'seats': 4,
        'fuel': 'gasoline',
        'gearbox': 'semi-automatic',
    },
    {
        'id': 1,
        'brand': 'brand1',
        'model': 'model2',
        'seats': 2,
        'fuel': 'gasoline',
        'gearbox': 'manual',
    },
    {
        'id': 2,
        'brand': 'brand2',
        'model': 'model1',
        'seats': 4,
        'fuel': 'diesel',
        'gearbox': 'semi-automatic',
    }
]

fleet = [
    {
        'id': 'AA111AA',
        'brand': 'brand1',
        'model': cars_model[0],
        'books': [1],
    },
    {
        'id': 'BB222BB',
        'brand': 'brand1',
        'model': cars_model[1],
        'books': [],
    },
    {
        'id': 'CC333CC',
        'brand': 'brand2',
        'model': cars_model[2],
        'books': [],
    }
]

#Tamaño maximo de reservations
total_reservation_length = 0

#Reservas
from models.reservation import Reservation
from models.test_reservation import TestReservation
from datetime import date

reserva_ejemploA = Reservation(TestReservation('Joe Doe', date(2025,1,25), date(2025,1,28), 'AA111AA'))
reserva_ejemploB = Reservation(TestReservation('Joe Doe', date(2025,1,25), date(2025,1,28), 'BB222BB'))
reserva_ejemploC = Reservation(TestReservation('Joe Doe', date(2025,1,25), date(2025,1,28), 'CC333CC'))

reservations = [reserva_ejemploA, reserva_ejemploB, reserva_ejemploC]