import calendar

# Take input from user
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Display the calendar
print("\nCalendar for", month, year)
print(calendar.month(year, month))