import schedule
import time
from passavailabilitymonitor.jobschedule import define_availability_job
from passavailabilitymonitor import config

schedule.every(config.SCHEDULE_INTERVAL_MINUTES).minutes.do(define_availability_job)

while True:
    schedule.run_pending()
    time.sleep(1)