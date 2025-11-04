from datetime import datetime
date = datetime(2024, 1, 15)
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_index = date.weekday()
print(days[day_index])