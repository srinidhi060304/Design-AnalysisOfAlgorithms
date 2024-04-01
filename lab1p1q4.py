def reverse_string(s):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s
    # Recursive case: reverse the substring starting from the second character
    # and append the first character to the end
    return reverse_string(s[1:]) + s[0]

# Test the function
s = input("Enter a string: ")
reversed_s = reverse_string(s)
print("The reverse of '{}' is: {}".format(s, reversed_s))
