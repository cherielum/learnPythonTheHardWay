# from sys import argv

# script, user_name = argv
# start = '> '

# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(start)

# print(f"Where do you live {user_name}?")
# lives = input(start)

# print("What kind of computer do you have?")
# computer = input(start)

# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}.  Not sure where  that is.
# And you have a {computer} computer. Nice.
# """)


# Trying to replicate Zork
from sys import argv

script, user_name = argv
start = '> '

print(f"""
    Hi {user_name} to ZORK. You are at WEST OF HOUSE
    This is an open field west of a white house, with a boarded front door.
    There is a small mailbox here.
    A rubber mat saying 'Welcome to Zork!' lies by the door.
    """)

print("Please type: open.")
print(f"What would you like to open, {user_name}?")
openDoor = input(start)

print(f"""
Alright, but {openDoor} is not a verb I recognize.
""")

print("What kind of computer do you have?")
computer = input(start)

print(f"""
Alright, so you said {likes} about liking me.

""")

