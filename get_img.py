import requests

url = "https://axmjqhyyjpat.objectstorage.eu-amsterdam-1.oci.customer-oci.com/n/axmjqhyyjpat/b/randomimages/o/cars%2F"

for _ in range(1,5):
    r = requests.get(url +str(_)+".png")
    with open(f"image{_}.png", "wb") as image:
        image.write(r.content)
        if r.status_code == 404:
            break


