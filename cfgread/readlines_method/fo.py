#!/usr/bin/python3

# Open a file
fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readlines()
print ("Read Line: %s" % (line))

line = fo.readlines(2)
print ("Read Line: %s" % (line))

# Close opened file
fo.close()
