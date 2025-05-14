#Python file created to fetch the base file of a phone list from our customers through a HTTP request.
<<<<<<< HEAD
import requests

def Phone():
    url = "https://axmjqhyyjpat.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axmjqhyyjpat/b/schoolbusiness-sharedfiles/o/profiles1.csv"
    response = requests.get(url)

    if response.status_code == 200:
        with open("phonelist/profiles1.csv", "wb") as f:
            f.write(response.content)
        print("The file has been downloaded locally as 'profiles1.csv'")
    else:
        print(f"Download failed: {response.status_code}")
=======
import os
import requests

def fetch_file():
    url = "https://axmjqhyyjpat.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axmjqhyyjpat/b/schoolbusiness-sharedfiles/o/profiles1.csv"
    folder_name = "exports"
    file_name = "phonelists.csv"
    os.makedirs(folder_name, exist_ok = True)
    file_path = os.path.join(folder_name, file_name)
    
    if os.path.exists(file_path):
        answer = input("File already exists. Do you want to overwrite it? (y/n): ").strip().lower()
        if answer == 'y':
            os.remove(file_path)
            print("Old file removed.")
        else:
            return "Download canceled by user."
    
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        return f"File downloaded and saved to {file_path}"
    else:
        return f"Download failed: {response.status_code}"
>>>>>>> 4ad23b633efaa67d1768d05214df1fd52626066d

