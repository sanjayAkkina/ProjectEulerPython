"""
PROBLEM 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
"""

response = input("Input Number: ")
sum = 0
counter = 0
print "Numbers Divisible by 3 or 5"
print "---------------------------"
for i in range(0,response):
    if (i % 3 == 0 or i % 5 == 0):
        print i,
        counter += 1
        if (counter == 5):
            print
            counter = 0
        sum += i

print "\n\nSum: ", sum
        