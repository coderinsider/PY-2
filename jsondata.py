#
import urllib.request
import json
def printResults(data):
	# Use the json module to load the string data into a directory
	theJSON = json.loads(data)

	# now we can access the contents of the JSON like any other python project
	if "title" in theJSON['metadata']:
		print(theJSON['metadata']['title'])
	# output the number of event, plus the magnitude and each event name
	count = theJSON['metadata']['count']
	print(str(count) + " events recordred")
	# for each event, print the place where it occurred
	for i in theJSON['features']:
		print(i['properties']['place'])
	# print the event that only have a magnitude greather than 4 
	for i in theJSON["features"]:
		if i["properties"]["mag"] >= 4.0:
			print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
	# Print Only the evetns where at least 1 person reported feeling somthiing
	print("Events that were felt: ")
	for i in theJSON["features"]:
		felthReports = i["properties"]["felt"]
		if felthReports != None:
			if felthReports > 0: 
				print("%2.1f" % i["properties"]["mag"], i["properties"]['place'], " reported " + str(felthReports) + " times")
def main():
	# Define a varaible to hold the source URL
	# In this case we'll use the free data feed from the USGS
	# This feed lists all earthquakes for the last day larger than Mag 2.5
	urlData = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'

	# Open the URL and read the data
	webURL = urllib.request.urlopen(urlData)
	if(webURL.getcode() == 200):
		data = webURL.read()
		printResults(data)
		print("Process Successful")
	else:
		print("Process Failed")

	print("Result code: " + str(webURL.getcode()))
if __name__ == "__main__" : main()