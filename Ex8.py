#Assigns literal string formatting to variable 'formatter'
formatter = "%r %r %r %r"

#prints numbers 1 to 4
print formatter % (1,2,3,4)
#prints strings one, two, three, four
print formatter % ("one","two","three","four")
#prints
print formatter % (True, False, False, True)
#print contents of variable formatter
print formatter % (formatter, formatter, formatter, formatter)
#prints 4 lines/strings
print formatter % (
"I had this thing",
"That you could type up right",
"But it didnt sing",
"So I said Goodnight"
)
