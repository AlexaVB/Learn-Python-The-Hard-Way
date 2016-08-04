#  Variables and Names

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# cars adds 100 to string
print "There are", cars, "cars available."

# drivers adds 30 to string
print "There are only", drivers, "drivers available"

# drivers takes 30 away from 100 and returns 70
print "There will be", cars_not_driven, "empty cars today."

# carpool_capacity takes cars_driven which is drivers(30) and times it with space_in_a_car(4.0)
print "We can transport", carpool_capacity, "people today."

# passengers adds 90 to the string
print "We have", passengers, "to carpool today."

# passengers devided by cars_driven or divers
print "We need to put about", average_passengers_per_car, "in each car"

#  1 - I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4? It would return 120 instead of 120.0, it's less accurate
#  2 - Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.
#  3 - Write comments above each of the variable assignments.
#  4 - Make sure you know what = is called (equals) and that it's making names for things.
#  5 - Remember that _ is an underscore character.
#  6 - Try running python from the Terminal as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
