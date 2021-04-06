#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

calc1 = 0.0
calc2 = 0.0
operation = ""

# while first operator is not "Q", print
while calc1 != "Q":
    print("\nWhat is the first operator? Or, enter Q to quit: ")
# if input is "Q", break out, otherwise, continue...    
    calc1 = input()
    if calc1 == "Q":
        break
    calc1 == float(calc1)
# if input is "Q", break out, otherwise, continue...
    calc2 = input("What is the second operator? or, enter Q to quit:\n")
    if calc2 == "Q":
        break
    calc2 = float(calc2)
    print("\nEnter an operation to perform on the two operators (+ or -): ")
 # if input is "+", add the operators   
    operation = input()
    if operation == "+":
        add = float(calc1) + float(calc2)
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(add))
 # if input is "-", subtract operator 2 from operaor 1   
    elif operation == '-':
        subtract = float(calc1) - float(calc2)
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(subtract))
 # any other input, print "Not a valid entry. Restarting..."   
    else:
        print("\nNot a valid entry. Restarting...")
# This still needs work, when asked for first operator and a string is entered, there is an error...
