def cheese_and_crackers(cheese_count, box_of_crackers):       #defines the function cheese_and_crackers
    print "We have %d cheeses!" % (cheese_count)              #prints out the cheese_count value
    print "We have %d boxes of crackers" % (box_of_crackers)    #prints out the box_of_crackers value
    print "Man, thats enough for a party"                     #programmerhumor
    print "Get a blanket.\n"                                  #programmerhumor with a new line


print "we can give the function numbers directly:"            #prints out using the direct values (method 1)
cheese_and_crackers(20, 30)                                   #provide the function with direct values as arguments


print "Or, we can use variables from our script:"             #prints out using variables (method 2)
amount_of_cheese = 10                                         #creates variables and gives it values
amount_of_crackers = 50                                       #creates variables and gives it values

cheese_and_crackers(amount_of_cheese,amount_of_crackers)      #calls the function and passes the variables


print "we can even do math inside"                             #prints out using math (method 3)
cheese_and_crackers(10+20,5+6)                                 #calls the function and gives math equation as values


print "We can give them numbers and do math as well"           #prints out using a combo of variables and math(method 4)
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000) #calls the function and gives the combo

#Lessons learned:
#1.Be careful with syntax!
#2.Dont trust the error message blindly.
#We can give values to the functions in multiple ways,
# 1.direct numbers,2.variables,3.math functions,4.combination of variables and math)
