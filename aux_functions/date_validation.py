from datetime import date

def date_validation(date1: date, date2: date = None):
    date2 = date1 if date2 == None else date2
    
    return (date.today()<= date1 and date1 <= date2)