from datetime import date

today = date(2023,11,27)
print(today.isoformat())

actually = date.today()
print(actually.isoformat())

from datetime import timedelta

week = timedelta(days=7)
next_monday = today + week
print(today + week)

from datetime import time

now = time(3,15,00)
print(now)

from datetime import datetime
dtime = datetime(2023,11,27,3,16,30)
print(dtime.isoformat())
print(datetime.now().isoformat())