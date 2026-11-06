from datetime import date
from datetime import datetime
from datetime import timedelta

today = date.today()
print (today)

print ("Date component", today.day, today.month, today.year)

print (today.weekday())

print (datetime.today())

print (datetime.now())

now = datetime.now()

# Date Formatting
# www.strfti.me
# %y %Y = Year
# %a % A = Weekday
# %b %B = Month
# %d %D = day of Month

print (now.strftime("The Current year is %y %Y"))
print (now.strftime("The Current Weekday is %a %A"))
print (now.strftime("The Current Month is %b %B"))
print (now.strftime("The Current day is %d %D"))



# %c - locale's datetime
# %x = locale's date
# %X = locale's time
print (now.strftime("The locale's datetime is %c"))
print (now.strftime("The locale's date is %x "))
print (now.strftime("The locale's time is %X"))



# Time Formatting
# %I %H - 12/24 hr
# %M - Minutes
# %S - second
# %p - AM/PM

print (now.strftime("The locale's time is %I:%M:%S %p"))
print (now.strftime("The locale's time is %H:%M:%S %p"))



# Time Delta
print ("=========== Time Delta +===============")

print (timedelta(days=365, hours=5, minutes=10))

print ("After 365 days: ", now + timedelta(days=365))

print ("After 3 weeks and 2 days: ", now + timedelta(weeks=3, days=2))

print ("1 week ago: ", now + timedelta(weeks=-1))

t = datetime.now() - timedelta(weeks=1)
s = t.strftime( " %H:%M:%S %A %B %d, %Y" )

print ("1 week ago: ", s)


today = date.today()
birthday = date(today.year, 1, 12)
if birthday < today:
    print( f'Your birth already pass by {(today-birthday).days} days Ago')
    birthday = birthday.replace(year=today.year+1)

mybirthday = birthday-today  
print( f'Your birth is after {mybirthday.days} days')

# Calender
print ("=========== Calender +===============")
import calendar

c = calendar.TextCalendar(0) # Monday - 0
thestr = c.formatmonth(2026,10)
print ( thestr )

# for i in c.itermonthdays(2026,10):
#     print ( i )


for name in calendar.month_name:
    print( name )

for day in calendar.day_name:
    print( day)

for week in calendar.day_abbr:
    print( week )

# Find the first friday of each month

print("Find the first friday of each month")

for month in range(1,1):
    c = calendar.monthcalendar(2026, month)
    weekone = c[0]
    weektwo = c[1]
    if weekone[calendar.FRIDAY] != 0:
        Meetingdate = weekone[calendar.FRIDAY]
    else:
        Meetingdate = weektwo[calendar.FRIDAY]
    print (  Meetingdate)

print ("-------- ------------ -------------- ------------- ----------")

def count_days(year, month, day):
    cont = 0
    c = calendar.monthcalendar(year, month)
    # lent = len(c)
    
    for week in c:
        print(week[day])
        if week[day] != 0:
            cont += 1
    print (cont)

count_days(2026,10, 0)