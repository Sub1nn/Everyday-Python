import calendar

yy = 2012
month = 12

print(calendar.month(yy, month))

print(calendar.month_name[1])

print(calendar.month_abbr[2])
print(calendar.isleap(2012))
print(calendar.leapdays(2000, 2023))
print(calendar.calendar(2024))
# Returns the day of the week as an integer for the given date. Monday is 0 and Sunday is 6.
print(calendar.weekday(2012, 12, 25))

# Returns a string with the abbreviated names of the weekdays, where n is the width of the string.
print(calendar.weekheader(3))

# Returns a list of weeks for the given month and year, where each week is represented as a list of 7 integers. Days outside the month are represented as zeros.
print(calendar.monthcalendar(2024,12))

# Prints the calendar of the specified month and year to the console.
print(calendar.prmonth(2024,12))

# Prints the entire calendar for the given year to the console.
print(calendar.prcal(2024))

# Sets the first day of the week. The default is Monday (0), but you can set it to Sunday (6) or any other day.

print(calendar.setfirstweekday(calendar.SUNDAY))

# Returns the current setting for the first day of the week.
print(calendar.firstweekday())

# Generates a calendar in HTML format.
cal = calendar.HTMLCalendar(calendar.SUNDAY)
print(cal.formatmonth(2024, 12))

# Returns a plain text calendar. You can specify whether to start the week on Monday or Sunday.
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatmonth(2024, 12))

# Similar to TextCalendar, but it allows for localization of month and weekday names based on the locale.
cal = calendar.LocaleTextCalendar(calendar.SUNDAY, locale='en_US')
print(cal.formatmonth(2024, 12))

# Provides the basic functionality to work with calendars, and allows customization such as which day of the week to start on.
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
print(cal.monthdays2calendar(2024, 12))  # List of weeks, each with pairs (day, weekday)








