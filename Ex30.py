people = 30
cars =40
buses = 15

if cars >  people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We cant decide!"

if buses > cars:
    print "Thats too many buses"
elif  buses < cars:
    print "Maybe we should take the buses"
else:
    print "We still cant decide"

if people > buses:
    print "Allright, lets just take the buses"
else:
    print "Lets just stay in!"