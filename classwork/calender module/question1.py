'''
Write a program to print the year in the following format. The day of the week must start with
Sunday. Hint: calendar.setfirstweekday(weekday)
* One column calendar with a spacing of two lines between the weeks.
* Two column calendar with a column width of 6 characters.
* 4-column calendar with default spacings between columns and rows.
'''

import calendar
calendar.setfirstweekday(6) #Used to set  the callender start week
year = 2024
# print(calendar.calendar(year))
print("One column calendar with a spacing of two lines between the weeks: ")
calendar.prcal(year,w=0,l=2,c=6,m=1)

print("Two column calendar with a column width of 6 characters.: ")
calendar.prcal(year,w=6,l=0,c=6,m=2)

print("4-column calendar with default spacings between columns and row: ")
calendar.prcal(year,c=6,m=4)

