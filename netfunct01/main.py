#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# init initializes colorama, Fore, Back & Style
from colorama import init, Fore, Back, Style


# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        # prints with green text background
        print(Back.GREEN + 'Handshaking. .. ... connecting with ' + coffeetime )
        # resets styling - foreground and background colors
        print(Style.RESET_ALL)
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            # prints with cyan text
            print(Fore.CYAN + 'Attempting to sending command --> ' + mycmds )
            print(Style.RESET_ALL)
            # we'll learn to write code that sends cmds to device here

# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

# call our main function
main()




# starts our second function
def devicereboot():
    # a list of IP addresses
    ips = [ "14.113.5.26", "12.344.1.91", "21.987.6.54" ]
    # iterate through the list ips
    for x in range(len(ips)):
        print("Connecting to.." + ips[x])
        print("REBOOTING NOW!")
devicereboot()


# starts our third function

# Currently, the data processed by our program is assigned statically to the variable work2do. Create a new (better) mechanism for providing the input to the script (such as an external file). How you structure the data within the external file is upto you.

# NOTE: JSON is a fine choice, however, describing the data via YAML might be a better choice. YAML is human-readable version of JSON. The spec is available at https://yaml.org/spec/1.2/spec.html. You can import YAML data into python with the pyyaml library.

# When you're finished save your code.






















