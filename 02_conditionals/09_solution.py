year = 2024

if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print(year," is a leap year")
    print("congrats you have one more extra day in a year1")
else:
    print(year, " is Not a leap year")
