from datetime import date
from datetime import datetime

# para tomar la hora 
now = datetime.now()
today = date.today() 
today_2 = "{}/{}/{}".format(today.year, today.month, today.day)
now = datetime.now() 
time = "{}:{:02d}:{:02d}".format(now.hour, now.minute,now.second)

'''
    {% for error in form.from_cantidad.errors %}
                                            <p style="color: aqua;">
                                                {{ error }}
                                            </p>}}
                                        {% endfor %}
'''







