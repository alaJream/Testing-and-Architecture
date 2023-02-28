# by Kami Bigdely 
# Replace magic numbers with named constants

CONSTANT = 8.9875517923 * 1e9

# First Section
# Given two point charges, calculate the electric force exerted on them.
q1 = int(input('Enter a value of charge q1: '))
q2 = int(input('Enter a value of charge q2: '))
distance = int(input("Enter the distance between two charges: "))
force = CONSTANT * q1 * q2 / (distance ** 2)
print("Electric Force between q1 and q2 is: ", force, "Newton")

# Second Section, define constants
EVEN = "even"
ODD = "odd"

num = int(input('Enter an integer number: '))
if num % 2 == 0:
    print(num, "is an", EVEN, "number.")
else:
    print(num, "is an", ODD, "number.")
