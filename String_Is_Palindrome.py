def is_palindrome(s):
    # convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # check if the reversed string is equal to the original string
    return s == s[::-1]

# test the function
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))