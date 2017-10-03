#this one is like your scripts with argv
def print_two(*args):
    arg1,arg2= args
    print "arg1:%r, arg2:%r" % (arg1,arg2)

def print_two_again(arg1,arg2):
    print "arg1:%r, arg2:%r" % (arg1,arg2)

def print_one(arg1):
    print "arg1:%r" % (arg1)

#this one doesnt take any arguments
def print_none():
    print "I got nothing!"

print_two("Karthik","Dhoopati")
print_two_again("KP","Baba")
print_one("K")
print_none()

#This function assigns the argument to a parameter named bruce. When the function is called,
#it prints the value of the parameter (whatever it is) twice.
def print_twice (Bruce):
    print Bruce
    print Bruce

#For,example, "Jamal"
print_twice("Jamal")

def readfile(*args):
    filename = args
    txt = open.filename
    print read.txt

#readfile(Users/karthikdhoopati/Desktop/python programs/sample.txt)
