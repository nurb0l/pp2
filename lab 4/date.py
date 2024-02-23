#task 1
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print(new_date.strftime("%Y-%m-%d"))
#task 2 
from datetime import datetime, timedelta

current_date = datetime.now()

new_date = current_date - timedelta(days=1)

print(new_date.strftime("%Y-%m-%d"))

print(current_date.strftime("%Y-%m-%d"))

new_date = current_date + timedelta(days=1)

print(new_date.strftime("%Y-%m-%d"))
#task 3
from datetime import datetime 

current_data= datetime.now()

print(current_data.replace(microsecond=0))
#task 4
from datetime import datetime

date1 = input()
date2 = input()
date_1=datetime.strptime(date1, "%Y-%m-%d")
date_2=datetime.strptime(date2, "%Y-%m-%d")
    
time_difference = date_2 - date_1

seconds_difference = time_difference.total_seconds()
print(abs(seconds_difference))
