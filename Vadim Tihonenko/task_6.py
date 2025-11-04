import calendar
from datetime import datetime
def last_day(date):
    days = calendar.monthrange(date.year, date.month)[1]
    return days
date = datetime(2024, 2, 15)
print(f"{last_day(date)}(весокосный год)")