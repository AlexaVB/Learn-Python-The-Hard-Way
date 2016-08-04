people = 30
cars = 40
trucks = 15

if cars > people and False:
	print "We should take the cars."
elif cars < people or True:
	print "We should not take the cars."
	print "t"
else:
	print "We can't decide."

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
	print "t"
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
	print "t"
else:
	print "Fine, let's stay at home then"
