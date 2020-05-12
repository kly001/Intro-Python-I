"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

# cal = calendar.TextCalendar(calendar.SUNDAY)
# year = input("Pick a year:  ")
# month = input("Pick the number of a month(January=1; February=2; March=3; April=4; May=5; June=6; July=7; August=8;September=9; October=10; November=11; December=12 ):  ")
# # print(f'{int(year)},{int(month)}')
# input_year = int(year)

# int_month = int(month)
# str = cal.formatmonth(input_year,int_month)
# print(str)

# capture command line inputs
#  print the calendar
#  handle different numbers of command line arguments


today = datetime.today()

month, year = today.month, today.year

cal = calendar.TextCalendar(calendar.SUNDAY)

# print(sys.argv)

if len(sys.argv) ==1:
  calendar.prmonth(today.year, today.month)

elif len(sys.argv) == 2:
  calendar.prmonth(today.year, int(sys.argv[1]))

elif len(sys.argv) == 3:
  calendar.prmonth(int(sys.argv[2]), int(sys.argv[1]))

else:
  print("usage: filename month year")
  sys.exit(1)


## A. Johnson's Solution:

# Time related Variables
# newdate = datetime.today()
# cal = calendar.TextCalendar(firstweekday=6);
# # Formatted input
# x = [d.strip() for d in input("Enter comma-separated month and year in number format (ex., 5, 2020)... ").split(',')]
# x = None if x == [''] else x
# def print_cal(x):
#       if x == None:
#           print(cal.formatmonth(newdate.year, newdate.month))
#       elif len(x) == 1:
#           print(cal.formatmonth(newdate.year, int(x[0])))
#       elif len(x) == 2:
#           print(cal.formatmonth(int(x[1]), int(x[0]) ))
#       else:
#           print("PLEASE RE-ENTER the comma-separated month and year in number format (ex., 5, 2020)")
# print_cal(x)






