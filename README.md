# Support Scripts
Scripts for support.

# Bulk Gathering of locations
If you have a bunch of locations and need to gather their place IDs you can run the `getPlaceIds.py` script.

## Make sure you have python3 installed. 

Type in `python --version`. If something like `Python 3.X.X` shows up you're good! 
If not check out this link for installation instructions. https://realpython.com/installing-python/

## Install the virtual environment

This essentially ensures that all the code in here doesn't fuck with your computer. 
Make sure that you are in a terminal and are in the same directory as this repository.

1. Run `python -m venv env`. This creates your virtual environment.
2. Run `source env/bin/activate` from a Mac or `env\Scripts\activate.bat` in Windows. This activates your virtual environment.
3. Run `pip install -r requirements.txt`. This installs all the packages you need. 

## Bulk gathering of locations

Let's say you have a csv file with some columns like this 

`Name`	`Address Line 1`	`Address Line 2`	`City`	`State`	`Zip`

<br />

`Target` `123 Main Street`                `WhoVille` `NJ` `01234`

The `getPlaceIds.py` script can use that information to find the correct placeId 
and subsequently write that information to a new file. 

### Google API Setup

You need to have Google API Keys to execute the `getPlaceIds.py` script. 

To do so, navigate to https://cloud.google.com/resource-manager/docs/creating-managing-projects.
and follow the instructions.

Before proceeding, make sure you have:

1. Setup a project in Google Cloud Platform.
2. Setup API Keys and enabled Google Maps APIs for said API Keys. 
3. Setup Billing for your API Keys.

To test this you can just copy and paste this into a browser. Make sure to replace `<API-KEY>` with your API Keys:
`https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=mongolian%20grill&inputtype=textquery&fields=place_id&key=<API-KEY>`

If your response is the following, then you're ready to rock!
```
{
   "candidates" : [
      {
         "place_id" : "ChIJc8t5UHett4kRx7LC_lIvQiU"
      }
   ],
   "status" : "OK"
}
```
---------------------------------------------------------
To run `getPlaceIds.py` simply run the following from a terminal window:

`python getPlaceIds.py <API-Key> <File-To-Read-From> <File-To-Write-To>`

For example:

`python getPlaceIds.py AIzaSyD6Cj7hpNX0h-Y5Q1234-xD1234124E master_list_google_with_place_ids.csv output.csv`

In the above example:

Your API KEY is: `AIzaSyD6Cj7hpNX0h-Y5Q1234-xD1234124E `
The file that contains all the location data to start is: `master_list_google_with_place_ids.csv`
The name of the output file (which doesn't yet exist and will contain placeID information) is: `output.csv`


