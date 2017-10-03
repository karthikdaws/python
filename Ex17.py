#from module 'sys' import the 'argv' argument varible
from sys import argv
#from the module os.path import the 'exists' command.
from os.path import exists

#unpack the 3 passed arguments to script, from_file and to_file.
script, from_file, to_file = argv
#print a headsup of the activity
print "Copying from %s to %s" % (from_file, to_file)

#classic file manipulation of creating file object and then read the variable to content.
#opening a file and reading a file are two distinct/seperate steps.
in_file = open(from_file) #creating of variable 'in_file', for opening the file
indata = in_file.read()   #creation of variable indata,

#output the length of the input file because we have a file object ready.
print "The input file is %d bytes long" % len(indata)   #len is a function that measure lenght of string

print "Does the output file exist? %r" % exists(to_file) #exists is a function that checks for existence
print "Ready, hit RETURN to continue, CTRL+C to abort."
raw_input('?') #give the user a chance to give the confirmation.you can place a string inside to make it fancy

out_file = open(to_file, 'w') #open the target file in write mode
out_file.write(indata)        #write the file object to the target file

print "Allright! All Done!Please check"   #Output completion!

#close the source and target files.
out_file.close()
in_file.close()
