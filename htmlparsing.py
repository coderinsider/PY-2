from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):

	def main():
		f = open("samplehtml.html", "r")
		if f.mode == 'r': 
			print("Now file reading to ready")
			content = f.read()
			parser.feed(content)
		else:
			print("Now I cannot read your file. becase you format is " + str(f.mode))

	if __name__ == "__main__" : 
		main();