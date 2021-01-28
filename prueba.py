from datetime import date
from datetime import datetime

now = datetime.now()
today = date.today() 
today_2 = "{}/{}/{}".format(today.day, today.month, today.year)
now = datetime.now() 
time = "{}:{}:{}".format(now.hour, now.minute,now.second)



