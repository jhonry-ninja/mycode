#!/usr/bin/env python3

"""JCOpinaldo | Exploring Network Interfaces"""

import netifaces


def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message
main();

# Customization Request 01
def ip():
    message = 'The movie is about to begin, we recommend '
    adapter = float(input("What is your adapter name?"))

ip();

# Customization Request 02