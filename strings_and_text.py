# this line declares variable types_of_people which was 10
types_of_people = 10
# puts number 10 into a string and the f shows that the quote needs to look for a variable.
x = f"There are {types_of_people} types of people."

# this line declares variable binary to equal string "binary"
binary = "binary"
# this line declares variable to equal "don't"
do_not = "don't"
# this is a string with two strings injected into it by two variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# this string prints variable x which equals a string.
print(x)
# this string prints variable x which equals a string.
print(y)

# this string prints variable x which equals a string.
print(f"I said: {x}")
# this string prints quoted variable y which equals a string.
print(f"I also said: '{y}'")

# this variable equals a binary
hilarious = False
# this variable equals a quote that includes a binary variable
joke_evaluation = "Isn't that joke so funny?! {}"
# this prints a string and inserts variable wherever you want.
print("Isn't that {} joke so funny?! ".format("really"))

# this prints a string with a binary variable
print(joke_evaluation.format(hilarious))
# this is a variable that equals a string
w = "This is the left side of..."
# this is a variable that equals a string
e = "a string with a right side."

#this is two variables of string being printed out
print(w+e)