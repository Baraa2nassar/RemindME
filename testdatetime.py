import re,os
import sys
import datetime
import pytz
from pytz import timezone

#filename = input("filename: ")
eastern = timezone('US/Central')
now=datetime.datetime.now().astimezone(eastern)
remindMeAT =datetime.datetime(2021,7,8,16,11)  #year,month,day,hour,min,sec

week= datetime.timedelta(days = 7)
hour = datetime.timedelta(hours = 9)

my_date = datetime.datetime.now(pytz.timezone('US/Eastern'))

#print(now)
now = now.replace(tzinfo=None)

#print(my_date)
print(now)
#print(now.strftime("%Y-%m-%dT%H:%M:%S"))


print (" " + (now.strftime("%A at %I:%M%p -- %h/%d/%Y ")))
#print(now.strftime("%I:%M%p"))
#print(now)

#print(now+hour)

#print (dayo)