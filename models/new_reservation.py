from pydantic import BaseModel
from datetime import date

class New_Reservation(BaseModel):

    user: str
    date_init: date
    date_finish: date
    car_id: str