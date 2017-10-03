my_name = 'karthik dhoopati'
my_age = 34
my_height = 70
my_weight = 150
my_teeth = 'white'
my_eyes = 'black'
my_hair = "black"


print "lets talk about %s" % my_name
print "he is %d inches tall" % my_height
print "he is %d pounds heavy" % my_weight
print "Actually thats not too heavy"
print "He has got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth
#This line is tricky , try to get it right
print "If I add %d, %d, and %d I get %d" %(my_age,my_height,my_weight,my_age + my_height + my_weight)


#convert to cms and kgs
height_cm = my_height * 2.54
weight_kgs = my_weight * 0.453

print "Karthik heigh is %d in cms" %(height_cm)
print "Karthiks weight is %d in kgs" %(weight_kgs)
