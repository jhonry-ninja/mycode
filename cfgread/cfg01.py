#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
#print(configfile.read()) # NOTE: Commented out to exclude extra linefeed when for-loop prints value of x

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
#print(configlist) # NOTE: Commented out to exclude extra linefeed when for-loop prints value of x

## Iterate thrhough configlist
for x in configlist:
    print(x.strip()) # NOTE: Appended .strip() to x to remove extra whitespace

## Always close your file
configfile.close()

