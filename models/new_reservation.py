from pydantic import BaseModel
from datetime import date

class New_Reservation(BaseModel):

    usuario: str
    date_init: date
    date_finish: date
    car_id: str