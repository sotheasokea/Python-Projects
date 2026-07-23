from datetime import datetime, date, time, timedelta, timezone

#datetime = year-month-date hour:minute:second
now = datetime.now()
print(now)
print(now.year)
print(f"{now.month:02d}") #f"{expression}"
print(f"{now.day}")
print(now.hour)
print(now.minute)
print(now.second)

#date
date = date(2004, 6, 6)
print(date)
print(date.isoweekday())    # 1, 2, 3, 4, 5, 6, 7
print(date.weekday())       # 0, 1, 2, 3, 4, 5, 6

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#these two are the same
print(days[date.isoweekday()-1])
print(days[date.weekday()])

print(date.year, date.month, date.day)

#time
time = time(12, 0, 0)
print(time)
print(time.hour, time.minute, time.second)

#timedelta
timedelta1 = timedelta(
    days=4,
    seconds=67,
    microseconds=23,
    milliseconds=32,
    minutes=7,
    hours=21,
    weeks=6
)
print(timedelta1)

#default argument days
timedelta2 = timedelta(365)
print(timedelta2)

birthday = timedelta2 + date
print(birthday)


days_test = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# using enumerate function help us output the array, string, ... without tracking the index
for index, day in enumerate(days_test):
    print(index," ", day)
