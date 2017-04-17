# Note: all comments refer below.
# establishes total number of cars
cars =100
# establishes total capacity of 1 car
space_in_a_car = 4.0
# establishes total drivers available
drivers = 30
# establishes total passengers
passengers = 90
# Defines that cars not drive equals cars minus drivers # distinguishes between drivers and passengers, that these are distinct sets
cars_not_driven = cars - drivers
# Defines that cars_driven MUST equal amount of drivers, unchangeable.
cars_driven = drivers
# Defines carpool capacity as the number of cars driven multiplied by space in a car, 4.0
carpool_capacity = cars_driven * space_in_a_car
# Defines average passengers per car as passengers divided by cars driven
average_passengers_per_car  = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be" , cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "people to carpool today." 
print "We need to put about", average_passengers_per_car, "in each car."
