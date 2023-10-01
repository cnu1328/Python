'''import time

print('number of seconds happend till 12am of jan 1, 1970 : ', time.time())

lt = time.localtime(time.time())
print('local time is : ', lt)

print('formatted local time : ', time.asctime(lt))

lt = time.asctime(time.localtime(time.time()))
print(lt)

time.sleep(1)

lt = time.asctime(time.localtime(time.time()))
print(lt)

t = (2021,11,20,20,15,57,59,8,0)
second = time.mktime(t)
print(second)

t = time.mktime(t)

print('Time is specified string format ...', time.strftime('%b %d %Y %T', time.gmtime(t)))


import time

print(time.altzone)
t = (2021,11,20,20,15,57,59,8,0)
print(time.asctime(t))

#print(time.clock())

print(time.ctime(1637419557.0))

print(time.gmtime(1637419557.0))

print(time.localtime(time.time()))

print(time.mktime(t))

time.sleep(2)
t = (2021,11,20,20,15,57,59,8,0)
t = time.mktime(t)
print(time.strftime('%b %d %Y %T',time.gmtime(t)))



#print(time.strptime(time.gmtime(t),'%A %b'))

print(time.time())

#attributes
print(time.timezone)

print(time.tzname)



import calendar

print(calendar.calendar(2022))

print(calendar.firstweekday())

print(calendar.isleap(2020))

print(calendar.leapdays(2000,2100))

print(calendar.month(2021,11))

for i in calendar.monthcalendar(2021,11):
    print(i)


print(calendar.monthrange(2020,11))


calendar.prcal(2020,1,1,3)

calendar.prmonth(2020,11)

print(calendar.setfirstweekday(3))

t = (2020,11,21,3,2,6)

print(calendar.timegm(t))

print(calendar.weekday(2021,11,22))'''

import time
print(time.altzone)
print(time.asctime())
lt = time.asctime(time.localtime(time.time()))
print(lt)
print(time.time())
print(time.localtime())
print(time.ctime()) #asctime and ctime both are similar. Next using local time in between asctime also similar to asctime.
print(time.asctime(time.localtime()))
print(time.gmtime())
print(time.asctime(time.gmtime()))
print(time.time())
time.sleep(1)
print(time.mktime(time.gmtime()))
t=(2022,2,1,20,15,57,59,8,0)
t = time.mktime(t)
print(time.strftime('%b %d %Y %T',time.gmtime(t)))
#print(time.strptime(time.mktime(t),'%A %b'))

import calendar
print(calendar.calendar(2022))
print(calendar.firstweekday())
print(calendar.isleap(2020))
print(calendar.leapdays(2020,2030))
print(calendar.month(2022,11))
for i in calendar.monthcalendar(2022,11):
    print(i)
print(calendar.monthrange(2022,1))
t = calendar.setfirstweekday(2)
print(t)
print(calendar.weekday(2022,11,22))
print(calendar.weekday(2021,11,22))























































