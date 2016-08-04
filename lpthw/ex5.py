# Exercise 5: More Variables and Printing

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 * 2.54 # inches / cms
weight = 180.00 * 0.453 # lbs / kilo
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# replaces %s with a string, a string called name for example
print "Let's talk about %s." % name
print "He's %d cms tall." % height 
print "He's %d kilos74 heavy." % weight 
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#  this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
# Python format characters https://docs.python.org/2/library/stdtypes.html#string-formatting-operations

# http://stackoverflow.com/questions/2354329/whats-the-meaning-of-r-in-python
print repr('hi') # notice the quotes here as opposed to...
print str('hi')


class Foo:

  def __init__(self, foo):
    self.foo = foo

  def __eq__(self, other):
    """Implements ==."""
    return self.foo == other.foo

  def __repr__(self):
    # if you eval the return value of this function,
    # you'll get another Foo instance that's == to self
    return "Foo(%r)" % self.foo  	