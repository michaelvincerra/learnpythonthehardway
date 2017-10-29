# at beginning of script, this calls which modules will be utilized in the code
# visit this website to learn about the "sys" module: http://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script
from sys import argv

# this encapsulates two things, script and filename to call out the module contents in "argv" or argument variables
script, filename = argv

# Per Zed, this creates a "file object" but it does NOT "return the contents of a file."
txt = open(filename)

# where "filename" becomes the input variable referenced in the command line

print(f"Here's your file: {filename}")
# instruction for T to read the filename contents
print(txt.read())

# where command prompts user to type in the filename again in order to see the file contents
print("Type the filename again:")
file_again = raw_input(">> ")

# command to execute opening of filename entered
txt_again = open(file_again)

# command to DISPLAY the contents of filename
print(txt_again.read())
