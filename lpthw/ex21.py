# functions with arguments a and b 
def add(a, b):
# prints string with variables a and b 
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some maths with just functions!"

# variables with values for a and b
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# prints string with values from variables
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is the puzzle."

# variable with new variables inside
# starts backwards so with devide by 2
# devide by 2
# inside variable devide, 100 / 2 = 50
# inside variable multiply, 80 * 2 = 180
# inside variable subtract, 78 - 4 = 74
# inside variable add, 30 + 5 = 35

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

small_div = divide(iq, 2)
medium_mul = multiply(weight, small_div)
big_sub = subtract(height, medium_mul)

what = add(age, big_sub)

print "That becomes: ", what, "Can you do it by hand?"
