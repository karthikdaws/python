#Ex15.py
#importing argv from sys module
from sys import argv

#unpacking the 2 arguments into script and filename
script, filename = argv

#defining variable txt and creating a file object by opening the file
txt = open(filename)

#printing out the content of txt using txt.read()
print "Here is file %r:" % filename
#its possible to run a read function on a text file.
print txt.read()
print txt.close()

#prompt the filename again, this time using raw_input
print "Type the filename again:"
file_again = raw_input (">")

#This time save the contents of the file to a variable called txt_again
txt_again = open (file_again)

#print the contents of the variable txt_again using read()
print txt_again.read()
print txt_again.fileno() #outputs the fileno
print txt_again.isatty() #outputs whether a tty device is attached
print txt_again.close() #closes the file that has been opened.

#So there are atleast two ways to open a file.
#Method 1 is to ask the user to pass the filename as a parameter and
#save the passed parameter in argv, create a file object using a variable,and a perform a read function on the
#variable.
#Method 2 is to prompt the user for the filename, save the user's input in a variable,and perform a read
#function on the text object.
#1.Get filename from user, create a file object and save it in a variable, perform a read on that variable.
