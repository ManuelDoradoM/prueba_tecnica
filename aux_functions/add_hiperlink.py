from datetime import date

def add_hiperlink(car: dict, date1: date, date2: date):

    car_copy = car.copy()
    
    car_copy['_links'] = {
            'href': r'/booking',
            'method': 'POST',
            'description': 'Endpoint para crear una reserva',
            'body_schema': {
                'type': 'New_Reservation',
                'properties': {
                    'usuario': {'type': 'string'},
                    'date_init': {'type': 'date'},
                    'date_finish': {'type': 'date'},
                    'car_id': {'type': 'string'}
                },
                'requiered': ['usuario', 'date_init', 'car_id']
            }
    }
    return car_copy
