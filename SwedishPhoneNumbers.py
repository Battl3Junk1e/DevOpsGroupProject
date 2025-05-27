import csv
import requests
import os
import fetch_phone_list
import pprint

# Creates function to use in main file
def SwedishPhoneList():
    filepath = "exports/phonelists.csv"
    if not os.path.exists(filepath):
        print (f"file not found: {filepath}")
        print ("Please run the phoneGetFile first to download the CSV file.")
        return []
    else:
    # Open/Read the CSV File
        with open(filepath, encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)

            # Get the relevant headers
            headers = next(reader)
            print("Headers:", headers)

            # Find indexes of relevant columns
            firstname_idx = headers.index("Givenname")
            lastname_idx = headers.index("Surname") 
            tel_idx = headers.index("Telephone")
            land_idx = headers.index("Country")

            print("")
            SwedishList = []
            # Loop through each row and filter for Swedish contacts
            for row in reader:
                if row[land_idx] == "Sverige":
                    SwedishList.append(f"Name: {row[firstname_idx]}, Last Name: {row[lastname_idx]}, Phone: {row[tel_idx]}, Country: {row[land_idx]}")
        pprint.pprint(SwedishList)
        return