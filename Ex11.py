#Ex11
print "How old are you?",        #ask the user his age
age = raw_input()               #take what they type and store it in variable 'age'
print "How tall are you?",      #ask the user his height
tall = raw_input()              #store the users input in a varibale called 'tall'
print "How much do you weigh?", #ask the user his weight
weight = raw_input()            #store the user input in a variable called 'weight'

#using literal string formatting, print out the values in the variables age, tall and weight, as inputed by the user.
print "So, you are %r years old, %r inches tall and your weight is %r lbs " %(age, tall, weight)

#Prints out the values stored in the variables.
print "So, you are",age, "years old",tall, "inches tall and your weight is", weight, "lbs"
