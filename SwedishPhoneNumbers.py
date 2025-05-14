import csv
import requests
import os
import fetch_phone_list

# Creates function to use in main file
def SwedishPhoneList():
    filepath = "export/phonelists.csv"
    if not os.path.exists(filepath):
        print (f"file not found: {filepath}")
        print ("Please run the phoneGetFile first to download the CSV file.")
        return []
    # Open/Read the CSV File
    with open("profiles1.csv", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        # Get the relevant headers
        headers = next(reader)

        # Find indexes of relevant columns
        firstname_idx = headers.index("Givenname")
        lastname_idx = headers.index("Surname") 
        tel_idx = headers.index("Telephone")
        land_idx = headers.index("Country")

        print("\nSwedish telephone numbers:")
        SwedishList = []
        # Loop through each row and filter for Swedish contacts
        for row in reader:
            if row[land_idx] == "Sverige":
                SwedishList.append(f"Name: {row[firstname_idx]}, Last Name: {row[lastname_idx]}, Phone: {row[tel_idx]}, Country: {row[land_idx]}")
    return SwedishList
