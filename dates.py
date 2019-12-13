# Example file for working with date information
from datetime import date
from datetime import time
from datetime import datetime
def main():
	# Get today's date from the simple today() method from the date class
	print('Hello')
	today= date.today()
	print("Today date is ", today)
	# print out the date's individual components
	print("Date components: ", today.day, today.month, today.year)
	# retrieve today's weekday (0=monday, 6=sunday)
	dateformat = today.weekday()
	if(dateformat == 4):

		print("Today's weekday # is Friday")
	days=['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
	print("Which is a: ", days[dateformat]);
	## Date time Objects
	# Get today's date form the date time class
	today = datetime.now()
	print("The current date and time is: ", today)

	# Get the current time
	t = datetime.time(datetime.now())
	print(t)

if __name__ == "__main__":
	main()	