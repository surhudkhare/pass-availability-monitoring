import schedule
import time
from datetime import timedelta
from passavailabilitymonitor import config
from passavailabilitymonitor.monitoring import check_availability
from passavailabilitymonitor.notification import notify

def define_availability_job(trail, target_date, mode="test"):
    print(f"Monitoring {trail} for {target_date} in {mode} mode")
    if check_availability(trail=trail, target_date=target_date, mode=mode):
        notify()

if __name__ == "__main__":
    # Using input
    print("This tool helps you automatically monitor the availability of trail passes on the BC parks website.\nPress 'Ctrl+C' to exit/stop execution.")
    mode = input("Enter T for Test mode and L for Live: ")
    if mode == "T":
            schedule.every(10).seconds.until(timedelta(minutes=10)).do(define_availability_job, trail="Test trail", target_date="Test date", mode="test")
    elif mode == "L":        
        trail_name = input("Please enter trail name: ").lower()
        target_date = input("Please enter target date in the format YYYY-MM-DD: ")
        schedule.every(1).minutes.until(timedelta(hours=3)).do(define_availability_job, trail=trail_name, target_date=target_date, mode="live")
    while True:
        # print(f"Start monitoring {trail_name} for {target_date} - {datetime.today().strftime("%d-%b-%Y %H:%M:%S")}")
        print(".", end="")
        schedule.run_pending()
        time.sleep(1)
