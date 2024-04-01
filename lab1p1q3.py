def string_to_integer(s):
    # Base case: if the string is empty, return 0
    if len(s) == 0:
        return 0
    # Recursive case: remove the leftmost digit, convert the remaining string to integer,
    # and append the leftmost digit multiplied by appropriate power of 10
    return int(s[0]) * 10**(len(s) - 1) + string_to_integer(s[1:])

# Test the function
s = input("Enter a string of digits: ")
result = string_to_integer(s)
print("The integer representation of '{}' is: {}".format(s, result))
