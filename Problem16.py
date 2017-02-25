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