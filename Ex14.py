#Ex14.py
from sys import argv

script, username = argv
prompt = '<Ans>'

print "Hi %s,I am the %s script" % (username, script)
print "I would like to ask you a few questions!"

print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where do you live %s?" % username
location = raw_input(prompt)

print "What kind of computer do you have %s?" % username
computer = raw_input (prompt)

print "What kind of car do you drive %s?" % username
car = raw_input (prompt)


print """
OK!, So you said  "%s" to liking me, live in %s, have %s computer and drive a %s car. Nice!
""" %( likes,location,computer,car )
