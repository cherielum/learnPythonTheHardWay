"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\n on a line." # Splits the line after the 'split' word.
backslash_cat = "I'm \\ a \\ cat." # need to backslashes to show one slash

fat_cat = """
I'll do a list:
\t* Cat food:
\t  * Fishies
\t  * Catnip\n\t    * Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# memorize below when possible
# Escape	What it does.
# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh