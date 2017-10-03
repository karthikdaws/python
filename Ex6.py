
#Assign values to cryptic variables,x, y, binary and do_not
x = "There are %d types of people." % 10
binary = "binary"
do_not = "dont"
y = "Those  who know %s and those who %s." %(binary, do_not)

#print assigned value of variables x and y
print x
print y

#print the literal representation of 'x' and the string representation of 'y'
print "I said: %r." % x
print "I also said: '%s'." % y


#Assign values to variables, hilarious and joke_evaluation
#Determine how funny this joke is and and allow evaluation to have a literal
hilarious = False
joke_evaluation ="Isnt this joke funny! %r"

#print the evaluation and insert the hilarious status into it
print joke_evaluation % hilarious

#Assign strings to variables w and e
w = "This is the left side of..."
e = "a string with a right side"

#print the concantenation of w and e.
print w + e
