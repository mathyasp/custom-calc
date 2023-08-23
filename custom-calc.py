# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 
from math import sqrt

def hypotenuse(a, b):
    c_squared = (int(a))**2 + ((int(b))**2)
    return sqrt(c_squared)

print("Pythagorean Theorem Calculator")

right_triangle = input("Does your triangle have one 90 degree angle? \n").lower()

if right_triangle == "yes":
    length_a = input("What is the length of side a? \n")
    length_b = input("What is the length of side b? \n")
    print(f"Your hypotenuse is {hypotenuse(length_a, length_b)}") 
else:
    print("I'm sorry, I am just a pythagorean theorem calculator")

   
# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!




