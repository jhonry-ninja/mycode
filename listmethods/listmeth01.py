#!/usr/bin/env python3

# create a list-object containing three items
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

# print list
print(proto)

# print second item in the list
print(proto[1])

# add d, n and s to list-object proto
proto.extend("dns")

# print list
print(proto)
