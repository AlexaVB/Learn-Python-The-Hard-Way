from sys import argv
# unpack arguments into argv
script, input_file = argv

# defines a function called print_all with the argument f, f is a file
def print_all(f):
# reads and prints the whole file
	print f.read()

# defines a function called rewind with the argument f, f is a file
def rewind(f):
# a function dealing in bytes, it moves the file to 0 bytes
	f.seek(0)

# defines a function print_a_line with the arguments line_count and the variable f
def print_a_line(line_count, f):
# prints the variables line_count and f.readline() 
# the file object advances every time .readline() is called, it reads a line
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

# prints string 
print "Now let's rewind, kind of like a tape."

# using the function rewind with argument current_file
rewind(current_file)

# prints string
print "Let's print three lines:"

# variable current_line prints the line number 1
current_line = 1
# each time print_a_line is run, it passes the variable current_line
print_a_line(current_line, current_file)

# adds 1 to variable current_line
current_line += 1
print_a_line(current_line, current_file)

# adds 1 to variable current_line
current_line += 1
print_a_line(current_line, current_file)