def main():
	# Open a file for writing and create it if it doesn't exist
	#f = open('readme.txt', 'w+')

	# Open the file for appending text to the end
	f = open('readme.txt', 'r')
	# Write some lines of data to the file
	#for i in range(10): 
	#	f.write("This is next append line " + str(i) + "\r\n")
	# close the file when done
	#f.close()
	#print("Complete file date insert done")

	# Open the file back up and read the contents
	if f.mode == "r":
		#contents = f.read()
		contents = f.readlines()
		for x in contents:
			print(x)
	else:
		contents = "It's not read mode"
	print(contents)
	print("Complete Process done")
if __name__ == "__main__": 
	main()