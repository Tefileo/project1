# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'
# Prompt user for input and Re-assign these
# name = input('what new name would you like?')
# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'
#Fourth Commit

from datetime import date, timedelta

name = "Tefileo"
last_name = "Stephens"
species = "Human"
eye_color = "Brown"
hair_colour = "Black"
age = 30

name = input('Please enter your first name here: ')
last_name = input('Please enter your last name here: ')
species =  input('Please enter your species here: ')
eye_color =  input('Please enter your eye color here: ')
hair_colour =  input('Please enter your hair colour here: ')
age = int(input('Please enter your age in years: '))

print('Hello {} {}! Thank you for confirming your species to be {}, your eye colour to be {}, and your hair colour to be {}.'.format(name, last_name, species, eye_color, hair_colour))

print('You tolommid us you are {} years old, this must mean you where born in {}.'.format(age, 2020-age))