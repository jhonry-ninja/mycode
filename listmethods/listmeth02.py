#!/usr/bin/env python3

proto = ["ssh", "http", "https"] # a list of common protocols
protoa = ["ssh", "http", "https"] # a list of common protocols
print(proto)

#proto.append("dns") # this line will add "dns" to the end of our list
#protoa.append("dns") # this line will add "dns" to the end of our list
#print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports
#proto.extend(proto2) # pass proto2 as an argument to the extend method
#print(proto)

protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

proto.insert(0, "ftp") # inserts item before the first item on the list or inserts item at the front of the list 
print(proto)

proto.insert(1, "ftp") # inserts item before second item on the list
print(proto)



