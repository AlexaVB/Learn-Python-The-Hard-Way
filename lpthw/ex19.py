# defines a function called cheese_and_crackers
# the function has two arguments cheese_count and boxes_of_crackers 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# prints string with cheese_count
	print "You have %d cheeses!" % cheese_count
# prints string with boxes_of_crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
# \n end of line, line space
	print "Get a blanket.\n"

# prints first string with the two values inserted directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# adds the values to the variables in the script
print "OR, we can use the variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# uses maths to work out the total for each (30 and 11)
print "We can even do maths inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# takes each variable and adds a value using maths
print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def krakow_weather(day, temperature, chance_of_rain):
	print "It is %s!" % day
	print "The temperature outside is %d!!!" % temperature
	print "And the chance of rain is %s" % chance_of_rain
	print "Take a jacket!\n"

print "Give the function numbers directly:"
krakow_weather("Wednesday", 13, "90%")

print "use the variables from our script:"
day = "Sunday"
temperature = 17
chance_of_rain = "5%"

krakow_weather(day, temperature, chance_of_rain)

print "We can even do maths inside too:"
krakow_weather("sunday", 5 + 5, 1 + 3)


