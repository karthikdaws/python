from sys import argv                            #from sys module, import function argv

script, input_file = argv                       #set up the script for one variable 'input_file'

def print_all(f):                               #defines function 'print_all' which prints the file object
    print f.read()

def rewind(f):                                  #defines function 'rewind',which moves cursor to row no 1 of file object.
    f.seek(0)

def print_a_line(line_count, f):                #defines function 'print_a_line' which takes arguments line_count and f
    print line_count, f.readline()              #prints the

current_file = open(input_file)                 #creates a variable called current_file which opens the file.

print "First lets print the whole file:\n"      #Prints the whole given file

print_all(current_file)                         #calls function print_all on the variable current_file

print "Now lets rewind, kinda like a tape!"     #announces the rewind function.

rewind(current_file)                            #calls the rewind function on the variable current_file

print "Now lets print three lines:"             #announces that next 3 lines will be printed
#index current line
current_line =1                                 #creates a variable called current_line and passes the value of 1
print_a_line(current_line,current_file)         #calls function print_a_line and passes 1, and current line as values
#increment current line by 1
current_line = current_line+1                   #updates the values of current_line
print_a_line(current_line,current_file)         #calls function print_a_line and passes +1, and current line as values
#increment current line by 1
current_line = current_line+1                   #updates the values of current_line
print_a_line(current_line,current_file)         #calls function print_a_line and passes +1, and current line as values



#NEW STUFF!
#f is a file object!
#f.read/f.seek/f.readline are functions that can be performed on the file object.
#you can manipulate the read head to read specific lines in a file
#a variable can be be incremented on its former self.
