import datetime
currDate= datetime.datetime.now()
year=int(input("year: "))
month=int(input("month: "))
day=int(input("day: "))
x=datetime.datetime(year, month, day)

if(currDate.date()>x.date()):
    print(str(x.date())+" was in the past")
elif(currDate.date()<x.date()):
    print(str(x.date())+" is in the future")
else:
    print(str(x.date())+" is today")
