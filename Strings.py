# Strings are effectively arrays of single letters

old_string = "banana"
new_string = old_string.upper()
print(new_string)

# Casing methods
# .upper() makes all letters uppercase
# .lower() makes all letters lowercase
# .capitalize() makes the first letter uppercase
# .isupper() returns true if every letter is uppercase, false if not
# .islower() returns true if every letter is uppercase, false if not

# Character methods
# .isalpha() returns true if every character is a letter, false if not
# .isnumeric() returns true if every character is a number, false if not
# .isalnum() returns true if every character is either a letter or number, false if not

# Other methods
# .count() returns how many times a character is in a string
# .find() returns the first index that the character can be found in the string
# .rfing() returns the last index that the character can be found in the string

# Slicing
new_string = old_string[1:6:2] # slice [first index:last index:step(optional)]
print(new_string)

# Formatting
# .strip() removes trailing and leading whitespace from a string "  hi  " -> "hi"
# .replace(old,new) replaces all old values with new values
# .split(" ") splits them into separate items in the list depending on what character you put inside the quotes.
# most times it's space or commas
# "".join(string) joins separate items in a list into one string, separating them with each item that you provided
# f strings allow you to put expressions inside strings
# f"My name is {name}" where name = "Sam"

# Example problem: Leetcode 125
s = s.lower() #make all characters lowercase, this will help with
new_s = "" # initialize a new string to store the characters that we pick out from below

for char in s: #iterate through the string checking each character
    if char.isalnum(): # if the character is a letter or number
        new_s += char # store it in a new string

    return new_s == new_s[::-1] # if the new string is equal to new string sliced backwards, return true
