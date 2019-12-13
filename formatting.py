# Example file for formatting time and date output
from datetime import datetime
def main():
	print("datetime starting running.")
	now = datetime.now()
	print(now)
	# Times and dates can be formatted using a set of predefined string control codes

	### Date formatting###
	# %y/%Y - Year, %a/%A - Weekday, %b/%B - Month, %d - day of month
	print(now.strftime("The current time is: %Y - %a - %B - %d"))
	# %c - locale's date and time, %x - locate's date, %X - locate's time
	print(now.strftime("Locale date and time: %c"))
	print(now.strftime("Locale date %x"))
	print(now.strftime("Locale time: %X"))
	## Time Formatting

	# %I/%H - 12 / 24 Hour, %M - minute, %S - second, %p - locate AM/PM
	print(now.strftime("Current time: %I:%M%S %p"))
if __name__ == "__main__":
	main()