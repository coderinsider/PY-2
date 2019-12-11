#
# Example file for variables
#f=0
#print(f)

#f="abc"
#print(f)
# Declare a variable and initalize it

# Error variables of different type cannot be combined
print("This is a string: " + str(123))
# Global vs local variables in functions

def someFunction():
	f="def"
	print(f)

someFunction()
print(f)