import time
import schedule

from service.scrappy import job

if __name__ == '__main__':
    #schedule.every(3).hours.do(job)
    index=1
    #while True:
    while index < 2:
        job()
        #schedule.run_pending()
        time.sleep(1)
        print ("Enregistrement:", index)
        index += 1
