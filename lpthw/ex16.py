from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# open() is a function
# 'w' says open this files in the write mode
# ('r' for read mode and 'a' for append)
# the default for open(filename) is 'r'
target = open(filename, 'w')

print "Trucating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

print "Type the file again:"

file_again = raw_input("> ") 

text_again = open(file_again)

print text_again.read()

# There's too much repetition in this file. Use strings, formats, 
# and escapes to print out line1, line2, and line3 with 
# just one target.write() command instead of six.