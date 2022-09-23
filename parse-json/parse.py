import json
import os

# create absolute path

abs_dir = os.path.dirname(__file__)
print("The Script is located at:" + abs_dir )
file_absolute_path = os.path.join(abs_dir, 'parse.json')
print("The Script Path is:" + file_absolute_path)

#  parse JSON

json = json.loads(open(file_absolute_path).read())
value = json['name']
print(value)

# Loop through keys and values

for key in json:
    value = json[key]
    print("The key and value are ({}) = ({})".format(key, value))
    
    
# get a json from a remote API and parse it
import urllib.request as urllib2
import json
req = urllib2.Request("https://catfact.ninja/fact")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print (json)
fact = json['fact']
print (json['fact'])