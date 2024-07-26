import time
from datetime import datetime

def get_date_string(date):
    date_object = time.strptime(date, "%Y-%m-%d")
    return time.strftime("%A, %B %d, %Y", date_object)

def get_time_elapsed(start_time):
    
    return datetime.today()

def get_time():
    return datetime.today().strftime("%H:%M:%S %d-%b-%Y")

def get_date():
    return datetime.today().strftime("%Y-%m-%d")

if __name__ == "__main__":
    t = get_date()
    print(t)
    print(type(t))