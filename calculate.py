# Import the calendar module
import calendar

# Create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2019, 12, 4, 4) # formatmonth(Year, month, w, h)
#print(st)
# create an HTML Formatted Calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
hst = hc.formatmonth(2019, 12) # formatmonth(Year, month)
#print(hst)
# Loop over the days of a month
# zeroes mean that  the day of the week is in an overlapping month
#for i in c.itermonthdays(2020, 1):
	#print(i)

# The Calendar module provides useful untiltities for the given locale,
# Such as the names of days and months in both full and abbreviated forms 
# for cname in calendar.month_name:
# 	print(cname)
# for day in calendar.day_name:
# 	print(day)


# Calculate days based on a rule: for example, cosider
# a team meeting on the first firday of every month
# To figure out what days that would be for each month,
# We can use this script:
print("Team meetings will be on: ")
for m in range(1,13):
	cal = calendar.monthcalendar(2020, m)
	weekone = cal[0]
	weektwo = cal[1]
	weekthree = cal[2]
	weekfour  = cal[3]
	weekfive  = cal[4]

	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
		# More

	else:
		meetday = weektwo[calendar.FRIDAY]
	#print("%10s %2d" %(calendar.month_name[m], meetday))