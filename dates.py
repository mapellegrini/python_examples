#!/usr/bin/python

import datetime 
from dateutil.parser import parse


date1 = datetime.date(2001, 9, 11) 
date2 = datetime.date(2011, 4, 30) 
date3 = datetime.date.today()  

datetime1=datetime.datetime(2001, 9, 11, 23, 59, 59)
datetime2=datetime.datetime.now()
datetime3=parse("2009-01-05 22:14:39")

delta1=date3-date2
delta2=date3-date1
delta3 = datetime.timedelta(days=1, hours=1, microseconds=-1)

print "Dates"
for date in [date1, date2, date3]:
  print date

print "\nDatetimes:" 
for datetime in [datetime1, datetime2, datetime3]:
  print datetime, datetime.strftime("%d-%b-%Y"), datetime.isoformat()


print "\nDeltas:"
for delta in [delta1, delta2, delta3]:
  print delta
  print delta.days, delta.seconds, delta.microseconds




