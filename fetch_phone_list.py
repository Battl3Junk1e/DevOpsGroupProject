#Python file created to fetch the base file of a phone list from our customers through a HTTP request.
import os
import requests

def fetch_file():
    url = "https://axmjqhyyjpat.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axmjqhyyjpat/b/schoolbusiness-sharedfiles/o/profiles1.csv"
    folder_name = "exports"
    file_name = "phonelists.csv"
    os.makedirs(folder_name, exist_ok = True)
    file_path = os.path.join(folder_name, file_name)
    
    if os.path.exists(file_path):
        return "File already exists in the exports folder."
    
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        return f"File downloaded and saved to {file_path}"
    else:
        return f"Download failed: {response.status_code}"

