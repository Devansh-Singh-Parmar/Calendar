import calendar
def printcalendar(year):
    print(calendar.calendar(year))
year = int(input("Enter the year of which you want calendar: "))
printcalendar(year)