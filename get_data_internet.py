import urllib.request
import json

# Access the URL.

web_url = urllib.request.urlopen("http://www.example.com")

print ("Result Code: ", web_url.getcode() )

data = web_url.read()

# print (data)


# Get info using JSON Data

web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print ("Result Code: ", web_url.getcode() )
data = web_url.read()

# print (data)

theJSON = json.loads(data)

print ( theJSON["text"] )
print ( theJSON["id"] )
print ( theJSON["permalink"] )

