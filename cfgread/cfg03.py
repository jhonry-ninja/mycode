#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:

    # count lines
    count = len(open("vlanconfig.cfg", "rU").readlines())
    count = 0
    for line in open("vlanconfig.cfg", "rU").readlines():    
        count +=1

    load = configfile
    input("Please hit 'enter' and type the word 'load' to load the  file:  ")
    answer = input()
    print("You're looking for " + answer + ".") 

    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
    s1 = 'The vlanconfig.cfg file contains '
    s2 = ' lines. '

## file was just auto closed (no more indenting)



## each item of the list now has the "\n" characters back
print('\n'f'{configlist}')

# string concatenation using f-strings NOTE: so fresh 'n so clean
print('\n'f'{s1}' f'{count}' f'{s2}')
