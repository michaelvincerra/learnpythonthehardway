x = "There are 10 types of people."
binary = "binary"
do_not = "don't"
# string inside a string
y = "Those who know %s and those who %s" % (binary, do_not)

print(x)
print(y)
#  string inside a string
print("I said: %r." % x
#string inside a string)
print("I also said: '%s'.")

hilarious  = False
joke_evaluation = "Isn't that joke so funny?! %r"
#string inside a string
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side." 

# apparently, by using "print" w + e, it concatenates these two variables
print w + e
