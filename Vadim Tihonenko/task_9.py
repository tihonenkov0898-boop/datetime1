from datetime import datetime
date = datetime(2024, 1, 15, 14, 30, 45)
format1 = date.strftime("%d/%m/%y") 
format2 = date.strftime("%Y-%m-%d")  
format3 = date.strftime("%B %d, %Y")  
print(format1)
print(format2)
print(format3)