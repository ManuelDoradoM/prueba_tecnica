def del_books(car):
    
    car_copy = car.copy()
    del car_copy['books']
    return car_copy