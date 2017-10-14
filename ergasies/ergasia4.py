import requests
#url = "https://api.teleport.org/api/cities/"
url="https://api.teleport.org/api/cities/geonameid:5391959"
response = requests.request("GET", url)
print (response)