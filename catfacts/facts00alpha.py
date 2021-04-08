#!/usr/bin/env python3
"""JCOpinaldo | Pyton, APIs and JSON"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the methods available to our new object
    print( dir(r) )
main()
