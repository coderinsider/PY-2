# Example file for working with functions
def func1():
	print("I am function");

# Define a basic function

# function that takes arguments
def func2(arg1, arg2):
	print(arg1, " ", arg2)

# function that returns a value
def cube(x):
	return x*x*x
# function with default value for an argument
def power(num, x=1):
	result = 1
	for i in range(x):
		result = result * num
	return result

# function with variable number of argument
def multi_add(*args):
	result = 0
	for x in args:
		result = result + x
	return result

func1()
print (func1())
print(func1)
func2(10,20)
print('This is a print', func2(10,20))
print(cube(5))
print(power(2))
print(power(2,3))
print(power(x=3,num=5))
print(multi_add(1,2,3,4,5,6,7,8,9,10))