import time

def get_date_string(date):
    date_object = time.strptime(date, "%Y-%m-%d")
    return time.strftime("%A, %B %d, %Y", date_object)