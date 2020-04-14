#  CODED BY SAM@SAMEER
#  EMAIL:SAMS44802@GAMIL.COM
#  DATE:121/09/2019
#  PROGRAM: PRINTING OF CALENDAR

import calendar
year = int(input("ENTER THE YEAR :"))
print(f"*************** CALENDAR {year}***************")
cal = calendar.TextCalendar(calendar.SUNDAY)
i = 1
while i <= 12:
    cal.prmonth(year, i)  # PRE DEFINED FUNCTION
    i += 1
