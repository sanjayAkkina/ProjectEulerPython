"""
PROBLEM 6
The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum
"""

squareSumTotal = 0 #1^2 + 2^2 + ... + 10^2
sumSquareTotal = 0 #(1 + 2 + ... + 10)^2 
sumNaturalNumbers = 0

for i in range(1,101):
    squareSumTotal += i*i
    
for h in range(1,101):
    sumNaturalNumbers += h
    
sumSquareTotal = sumNaturalNumbers * sumNaturalNumbers

print "SUM OF THE SQUARES: ", squareSumTotal
print "SQUARE OF THE SUM: ", sumSquareTotal

print "DIFFERENCE: ", sumSquareTotal - squareSumTotal

