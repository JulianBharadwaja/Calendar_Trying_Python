import calendar
import datetime
import time

print(calendar.weekheader(3))
print() #new line

print(calendar.firstweekday())
print()

print(calendar.month(2020, 1))

print(calendar.monthcalendar(2020, 1))

print(calendar.calendar(2020))
#0 to 6 0 = monday
day_of_the_week = calendar.weekday(2020, 1, 22)
print(day_of_the_week)

is_leap = calendar.isleap(2020)
print(is_leap)
print()

how_many_leap_days = calendar.leapdays(2000,2001)
print(how_many_leap_days)