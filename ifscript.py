#!/usr/bin/env python3

message = 'You have chosen '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("Movie Roulette - Choose a number from 1-5 to watch a random movie: "))

# if input is equal to 1
if connection == 1:
    message = message + 'Harry Potter.'
elif connection == 2:
    message = message + 'Lord of the Rings.'
elif connection == 3:
    message = message + 'Chromicles of Narnia.'
elif connection == 4:
    message = message + 'The Notebook.'
elif connection == 5:
    message = message + 'Friday.'
else:
    message = message + 'one that is not available at the moment. Please try again.'
print(message)

