result = 1
temp = 1

while (temp != 10):
    for i in range (1,10):
        if (result % i == 0):
            temp += 1
        else:
            result += 1
            print "RESULT: ",result
            print "TEMP: ",temp
            break

#print result
            
            