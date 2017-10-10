types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "I don't"

y = f"Those who know {binary} and those who {do_not}." # These are the first and second places, in this exercise, where strings are embeded inside of strings.


print(x+y)
print(y)

print(f"I said: {x}")
print('I also said: {y}')

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation, tuple(do_not))

w = "This is the right side of..."
e = "a string with a left side."

print(w + e)