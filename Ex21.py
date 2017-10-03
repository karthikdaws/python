def add(a,b):
    print "ADDING %d + %d" %(a,b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d)" %(a,b)
    return a - b

def multiply(a,b):
    print "MULTIPLY %d * %d)" %(a,b)
    return a * b

def divide(a,b):
    print "DIVIDE %d / %d)" %(a,b)
    return a / b

print "Lets do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(43,3)
iq = divide(170,2)

print "Age:", age,"\nHeight:",height,"\nWeight:",weight,"\nIQ:",iq


#A puzzle for extra credit.

print "Here is a puzzle:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes",what,"can you do that by hand?"
