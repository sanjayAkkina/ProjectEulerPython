base = input("Input Base: ")
exponent = input("Input Exponent: ")

exponentFunction = base**exponent
tempNum = str(exponentFunction)
digitsArray = []

for digits in tempNum:
    digitsArray.append(int(digits))

print digitsArray

sum = 0

for i in digitsArray:
    sum += i

print "Sum of Digits: ", sum
    

"""
num = 2**15
tempNum = str(num)
array = []

for digit in tempNum:
    array.append(int(digit))
    
print array

sum = 0
for i in array:
    sum += i
    
print sum
"""