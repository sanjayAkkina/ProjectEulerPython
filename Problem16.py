"""
PROBLEM 16
What is the sum of the digits of the number 2^1000?

Modified to take user's response for the base
and the exponent for an exponential function
"""

base = input("Input Base: ")
exponent = input("Input Exponent: ")

exponentFunction = base**exponent
tempNum = str(exponentFunction) #Converts integer into a string
digitsArray = []

for digits in tempNum: #Stores digits into an array and converts into integers
    digitsArray.append(int(digits))

sum = 0

for i in digitsArray:
    sum += i

print "Sum of Digits: ", sum