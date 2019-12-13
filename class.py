# Example file for working with classes
class myClass():
	def method1(self):
		print("I'am working method1")

	def method2(self, someString):
		print("I am working method2" , someString)
def main():
	print("Ohh")
	c = myClass()
	c.method1()
	c.method2(" John Doe")

if __name__ == "__main__":
	main()
