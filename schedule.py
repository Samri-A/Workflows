import schedule
import time
def scheduleTask(when , date , task ):
    if(when == 'day'):
        schedule.every().day.at(date).do(task)


while True:
    schedule.run_pending()
    time.sleep(1)
    