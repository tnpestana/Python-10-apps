import datetime

# access current time
print(datetime.datetime.now())
print(type(datetime.datetime.now()))

# operations with dates
yesterday=datetime.datetime(2016,5,13,11,0,0,0)
now=datetime.datetime.now()
delta=now-yesterday
print(delta.days)
print(delta.total_seconds())
