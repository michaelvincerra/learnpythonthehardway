from sys import argv


script, filename = argv

txt = open(filename)

print(f"Here's your file: {filename}")

print(txt.read())

print(f"Type the filename again:")
file_again = input(">> ")

txt_again = open(file_again)

# print(txt_again.read())

txt_again.close()

# readme = f.close({filename})
#
