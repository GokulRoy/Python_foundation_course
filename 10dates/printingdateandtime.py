# importing by using keyword datetime
import datetime
a = datetime.datetime.now()
print(a)
# to print year
print(a.year)
# to print day in week
print(a.strftime("%A")) # to print in alfabet
print(a.strftime) # to print in location
b = datetime.datetime(2024,9,6)
print(b)