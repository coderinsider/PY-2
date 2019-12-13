# Example file for working with conditional statments

def main():
	x,y = 10, 100

	# Conditional flow use if, elif, else
	if( x < y ):
		st = "x is less than y"
	elif(x == y):
		st = "x is the same the y"
	else:
		st = "y is large than x"


	print(st)
	# Conditional statments let you see "a if C else B"
	st = "x is less than y" if (x < y) else "x is greater than y"
	print(st)
if __name__ == "__main__":
	main()