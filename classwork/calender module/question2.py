'''
Write a program to print the four leap years preceding and five leaf years succeeding of an year
entered by the user. Hint : Use calendar.isleap(year)
'''
import calendar

def findLeapYear(year):
    procced_leap_year = []
    succeed_leap_year = []

    y= year-1
    while len(procced_leap_year)<4:
        if(calendar.isleap(y)):
            procced_leap_year.append(y)
        y-=1
    y= year+1
    while len(succeed_leap_year)<5:
        if(calendar.isleap(y)):
            succeed_leap_year.append(y)
        y+=1
    return procced_leap_year,succeed_leap_year



year = int(input("Enter the year: "))
if calendar.isleap(year):
    print("The entered year is a leap year")
else:
    print("The given year is not a leap year")

preeced_leap_year, succeed_leap_year = findLeapYear(year)
print("The preceding years are: ",preeced_leap_year)
print("The succeding years are: ",succeed_leap_year)

    