formatter = "{} {} {} {}"


print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "This is the first line of my poem \n",
    "It is really great\n",
    "And I love it\n",
    "While ending with four lines"
))