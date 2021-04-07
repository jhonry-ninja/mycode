#!/usr/bin/env python3

# Pylint gets confused running code like the two lines below. It assumes the code willl be in a function. NOTE: It's better style to do work inside a function instead of at the top level. This allows you to better organize what you are doing and facilitates reusing it. You should really only have code performing an algorithm outside of a function in a quick and dirty script.

#mynote = "print this string"
#print(mynote)


# NOTE: The following is a better way:

"""
Author: JCOpinaldo

This program prints some things to the screen
"""

def main():
    """Our main program"""
    mynote = 'print this string' # define mynote
    print(mynote)                # display our string

main()

