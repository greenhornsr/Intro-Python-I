"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

# Variables
# System Args from Terminal
sysargs = sys.argv
# Create a calendar; store it in a variable object.
newcal = calendar.TextCalendar(firstweekday=0)
currdate = datetime.today()
month = currdate.month
year = currdate.year

def calendar_app(args):
  count = len(args)
  providedmonth = ""
  providedyear = ""
  if count == 1: 
    providedmonth = month
    providedyear = year
  elif count == 2:
    providedmonth = int(args[1])
    providedyear = year
  elif count == 3:
    providedmonth = int(args[1])
    providedyear = int(args[2])
  else:
    print("Please provide a file, month, year in that order.")
    return 
  newcal.prmonth(providedyear, providedmonth) 


# invoke the function
calendar_app(sysargs)
sys.exit()
