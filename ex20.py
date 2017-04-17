# imports python default arguments
from sys import argv

# identifies which file, input_file, is used as a variable among those argv
# get arguments
script, input_file = argv

# defines print_all function, which takes 1 argument (1)
def print_all(f):
	print f.read()
	
# defines the rewind function, which takes 1 argument (1)	
def rewind(f):
	f.seek(0)

# defines the print_a_line function, which takes 2 arguments (line_count, f) 
def print_a_line(line_count, f):
	print line_count, f.readline()
	
# set current_file variable to a file pointer to input_file
current_file = open(input_file)

#print/display string
print "First let's print the whole file:\n"

# call print_all function with current_file as an argument
print_all(current_file)

#print/display string
print "Now let's rewind, kinda like a tape."

# call rewind function with current_file as an argument
rewind(current_file)

#print/display string
print "Let's print three lines:"

# error occurs in lines 2 and 3 below, but I can't figure out what it is.
# set current_line to 1
current_line = 1
print_a_line(current_line, current_file)


# set current_line to itself + 1
# Zed shaw placed an error (?) in the call lines 2 and 3 below: 'current_line = current_line +1
current_line += 1
# call print_a_line function with current_line and current_file as arguments
print_a_line(current_line, current_file)


# set current_line to itself + 1
# Zed shaw placed an error  (?) in the call lines 2 and 3 below: 'current_line = current_line +1
current_line += 1
print_a_line(current_line, current_file)

