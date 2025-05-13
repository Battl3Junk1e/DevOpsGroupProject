#Python file created to fetch the base file of a phone list from our customers through a HTTP request.
import requests

url = "https://axmjqhyyjpat.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axmjqhyyjpat/b/schoolbusiness-sharedfiles/o/profiles1.csv"
response = requests.get(url)

if response.status_code == 200:
    with open("profiles1.csv", "wb") as f:
        f.write(response.content)
    print("The file has been downloaded locally as 'profiles1.csv'")
else:
    print(f"Download failed: {response.status_code}")

