def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are equal
    if s[0] == s[-1]:
        # Recursively check if the substring excluding the first and last characters is a palindrome
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the function
s = input("Enter a string: ")
if is_palindrome(s):
    print("'{}' is a palindrome.".format(s))
else:
    print("'{}' is not a palindrome.".format(s))
