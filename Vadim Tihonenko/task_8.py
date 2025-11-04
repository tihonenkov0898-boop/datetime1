from datetime import datetime
date_str = "2024-01-15 14:30:00"
date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(date)