# importing sys package. get the argv feature from the sys package.
from sys import argv

script, filename = argv

# variable txt is assigned to opening the file in this case reading_files_sample.txt
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