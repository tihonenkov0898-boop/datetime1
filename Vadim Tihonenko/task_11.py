from datetime import date, timedelta
def count_working_days(start, end):
    days = 0
    current = start
    while current <= end:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days
start_date = date(2024, 1, 1)
end_date = date(2024, 1, 31)
print(f"{count_working_days(start_date, end_date)} рабочих дней (исключая выходные)")  
