#!/usr/bin/env python3

# support for the urllib library
import urllib.request
# support for the RegEx library
import re

print("Where should we search?")

url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
# collect input for what to serach for
searchFor = input()
#urllib library to parse the URL entered by the user
searchMe = urllib.request.urlopen(url).read().decode("utf-8")
# reads as follows, "If searchFor pattern matches searchMe string"
if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")
