import datetime
from datetime import timedelta 
def going_date(NumberOfday):
    
        
    # format given date.
    gDate = datetime.date.today()
    
    # going  date 
    goingday = gDate + timedelta(days = NumberOfday)
    return goingday
    
def entry_date():
    entryDate = datetime.date.today()
    return entryDate