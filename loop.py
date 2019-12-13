# Example file for wroking with loops
import datetime
from datetime import date
# define a while loop
def main():
	x = 0
	while(x<10):
		print('This is while loop: ', x)
		x+=1 # x = x+1
	# define a for loop
	for x in range(5, 10):
		print('This is for loop', x)
	# use a for loop over a collection
	days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	for d in days:
		print("Days", d)
	print(date.today())
	# use the break and continue statements
	
	for x in range(5,10):
		# if(x==7): 
		# 	break
		# print(x)
		if(x% 2==0):
			continue
		print(x)

	# Using the enumerate() function to get index
	days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	for i,day in enumerate(days):
		print(day, " in index key is" , i)
# Result

if __name__ == "__main__":
	main()