#imports argv function from sys module
from sys import argv
#unpacks the 2 variables to argv
script, filename = argv
#confirms if the user wants to delete a file
print "We are going to erase %r." % filename
print "If you dont want that hit Cntl+c"
print "If you do want to do that hit RETURN"
#take a confirmation to truncate the file
raw_input("?")
#announces and truncated the file by opening the file in write mode and then running a truncate.
print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file!Good bye!"
target.truncate()
#prompts user for a new content
print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#write the new content to file
print "I am going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target = open(filename,'r')
print target.read()
#closes the file
print "Finally we close the file."
target.close()

#reopens the file to read it and closes it.
#newlist = open(filename)
#print newlist.read()
#print newlist.close()
