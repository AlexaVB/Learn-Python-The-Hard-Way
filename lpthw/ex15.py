# Get the argv feature from package sys
from sys import argv

# uses argv to get the file name
script, filename = argv

# opens txt file using the command open
txt = open(filename)

# prints the string with the file name
print "Here's your file %r:" % filename

# calls the function .read on txt file with no parameters
print txt.read()

print "Type the filename again:"

# takes the raw input (the file name) 
# and assigns it to the variable file_again
file_again = raw_input("> ")

# opens the file again using the variable file_again
txt_again = open(file_again)

# prints the file using the variable txt_again
print txt_again.read()