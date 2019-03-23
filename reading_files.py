# importing sys package. get the argv feature from the sys package.
from sys import argv

# creates an instance(?) of two argument variables.
# if you use argv, you have to use you have to use at least 1 argument variable for the script
# or two arguments, the first being the script. second being 'filename' here
script, filename = argv

# variable txt is assigned to opening the file in this case reading_files_sample.txt
# open() creates a file object which is called because of that function.
# txt becomes a file object of the file provided in the argument variable
txt = open(filename)

# prints out the file name
print(f"Here's your file {filename}:")
# prints out text within the file
print(txt.read())

# prints out text to ask for file name.
print("Type the filename again:")
# takes input
file_again = input("> ")

# declares another variable to open file
txt_again = open(file_again)
# prints out the text file before the program ends
print(txt_again.read())