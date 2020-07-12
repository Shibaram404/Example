from datetime import date,datetime
import time

while True:
    birtday = datetime(year=2021, month=2, day=5)
    countdown = birtday - datetime.now()
    print(countdown)
    time.sleep(1)
