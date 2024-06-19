import time
import schedule

from service.scrappy import job

if __name__ == '__main__':
    schedule.every(3).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
