import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
	# Print the name of the OS
	print(os.name)
	# Check for item existence and type
	print("Item exists: " + str(path.exists("readme.txt")))
	print("Item is a file: " + str(path.isfile("readme.txt")))
	print("Item is a directory: " + str(path.isdir("./")))
	# Work with file Paths
	print("Item path: " + str(path.realpath("readme.txt")))
	print("Item path and name" + str(path.split(path.realpath('readme.txt'))))
	# Get hte modificatino time
	t = time.ctime(path.getmtime('readme.txt'))
	print(t)
	print(datetime.datetime.fromtimestamp(path.getmtime('readme.txt')))


	# Calculate how long ago the item was modified

	td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("readme.txt"))
	print("It has been " + str(td) + " since the file was modified")
	print("Or, " + str(td.total_seconds()) + " seconds")
if __name__ == "__main__":
	main()