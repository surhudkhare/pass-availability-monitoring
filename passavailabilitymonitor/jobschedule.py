from passavailabilitymonitor.monitoring import check_availability
from passavailabilitymonitor.notification import notify

def define_availability_job():
    if check_availability(trail="CHEAKAMUS", target_date="2024-07-25"):
        notify()

