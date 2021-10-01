from Context_manager import MyContextManager
import calendar
import time

with MyContextManager():
    print(calendar.TextCalendar().formatyear(theyear=2020))
    time.sleep(3)

input()
