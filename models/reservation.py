from pydantic import BaseModel
from datetime import date
from database_placeholder import data_base


class Reservation(BaseModel):

    id: int
    usuario: str
    date_init: date
    date_finish: date
    car_id: str