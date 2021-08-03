"""Script to automatically generate place IDs.


You need to have an API Key to make this work. 

To do so, navigate to https://cloud.google.com/resource-manager/docs/creating-managing-projects.

Make sure you have:

1. Setup a project
2. Setup API Keys and enabled Google Maps APIs for said API Keys. 
3. Setup Billing for your API Keys

---------------------------------------------------------
To run this project simply run the following from a terminal window:

python getPlaceIds <API-Key> <File-To-Read-From> <File-To-Write-To>

For example:

python getPlaceIds AIzaSyD6Cj7hpNX0h-Y5Q1234-xD1234124E master_list_google_with_place_ids.csv output.csv

In the above example:

Your API KEY is: AIzaSyD6Cj7hpNX0h-Y5Q1234-xD1234124E 
The file that contains all the location data to start is: master_list_google_with_place_ids.csv
The name of the output file (which doesn't yet exist and will contain placeID information) is: output.csv


"""

import requests
import csv
import time
import sys

# Todo: Rename this
def readInFile(filename: str) -> dict:
	"""Reads in a file and generates a list of address strings.

	Parameters:
		filename: str
		Filename to be read out

	Note: This simply concatenates columns, so make sure the columns are
		  logically ordered from left to right to construct a search query.
	"""
	rows = []
	with open(filename) as f:
		reader = csv.reader(f, delimiter=",")
		line_count = 0
		for row in reader:
			# Skip the header
			if line_count == 0:
				line_count+=1
				continue
			else:
				rows.append(row)
			line_count+=1
	return rows


def getPlaceId(api_key: str, querytext: str):
	"""Gets a place ID for a provided query string.

	Parameters:
		querytext: str
			Example: "Kohl's 44200 Schoenherr Rd Sterling Heights MI 48313 USA"
		api_key: str
			API Key connected with your google project.

	"""
	url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
	response = requests.get(f"{url}input={querytext}&inputtype=textquery&fields=place_id&key={api_key}")
	print(f"Got a response {response.json()}")
	time.sleep(0.5)
	return response.json()


def getPlaceIds(api_key: str, filename: str, write_filename: str):
	"""
	Take in a filename and write the updated data with placeIds to write_filename.

	Parameters:
		filename: str
			Filename to be read from. Should be a csv.
		write_filename: str
			Filename to write to. Should be a csv.
		api_key: str
			API Key connected with your google project.
	"""
	rows = readInFile(filename)
	print(f"There are {len(rows)} total rows")
	placeIds = [getPlaceId(api_key, " ".join(row)) for row in rows]

	with open(write_filename, "w") as f:
		writer = csv.writer(f, delimiter=',')
		for row, placeId in zip(rows, placeIds):
			try:
				rowWithPlaceId = row + [placeId['candidates'][0]['place_id']]
				writer.writerow(rowWithPlaceId)
			except:
				print(f"Failed to find placeID for row {row}")


if __name__ == '__main__':
	api_key = sys.argv[1]
	read_filename = sys.argv[2]
	write_filename = sys.argv[3]
	getPlaceIds(api_key, read_filename, write_filename)
