from fastapi import APIRouter, HTTPException, responses
from database_placeholder import data_base

booking = APIRouter()

@booking.post('/booking')
def post_booking():
    pass