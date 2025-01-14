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


total_reservation_length = 0

#Reservas
from models.reservation import Reservation

from datetime import date


reservations = []