#variables with strings %d is replaced by 10
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# new variable y = a string and %s are replaced by the variables binary and do_not which has the strings "binary" and "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# prints variables x and y
print x 
print y

# prints a string and adds the string variable x 
print "I said: %r." % x
# prints a string and adds the string variable y
print "I also said: '%s'." % y

# variable is equal to false
hilarious = True 
# variable is equal to string. %r prints raw data of variable
joke_evaluation = "Isn't that joke so funny?! %r"

# prints above variables together
print joke_evaluation % hilarious 

# variables with strings
w = "This is the left side of..."
e = "a string with a right side."

# prints above variables together 
print w + e

# What is the difference between %r and %s?
# Use the %r for debugging, since it displays the "raw" data of the variable, but the others are used for displaying to users.