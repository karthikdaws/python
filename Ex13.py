#Ex13.py
#Parameters, unpacking variables

from sys import argv

zero, first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth = argv

print "The script is called:", zero
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third
print "The fourth variable is:", fourth
print "The fifth variable is:", fifth
print "The sixth variable is:", sixth
print "The seventh variable is:", seventh
print "The eight variable is:", eighth
print "The ninth variable is:", ninth
print "The tenth variable is:", tenth

opinion = raw_input("What did you think of this exercise?")
print "Thanks for your honest opinion: ", opinion
