print "How old are you?",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy" % (
    age, height, weight)

print "What day is it today?"
day = raw_input()
print "Where are you?"
answer = raw_input()
print "What did you learn?"
learnt = raw_input()

print "So, it\'s %r, and you\'re at %s and you learnt %s" % (
    day, answer, learnt)

# %r is a python object representation and %s turn it into a string
