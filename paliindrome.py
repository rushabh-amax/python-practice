# # original_string = "hello"
# # reversed_string = original_string[::-1]
# # print(reversed_string)


# for reverse string

# original_string = "jay"
# reversed_string = ""
# # J , 
# for char in original_string:
#     print("each character:",char)
#     reversed_string = char + reversed_string
#     # core logic
#     # " " = J + ""
#     # "J" = J + ""
#     # "J" = A + "J"
#     # "AJ" = Y " AJ"
#     # "YAJ" = x
#     print("after full reversed",reversed_string)
# print(reversed_string)  # Output: nohtyp



def is_palindrome(value):
    s = str(value)        # make sure it's a string
    reversed_s = ""       # empty string to build reverse
    
    for char in s:        # loop through each characterchar
        print(char)
        reversed_s = char + reversed_s   # add char in front
        print(type(s))
    
    return s == reversed_s


# print(is_palindrome("madam"))  # True

# print(is_palindrome(121))      # True

n = "naman"
s = str(n)
z = s[::-1]

# ternary operator to check palindrome
rev = "Palindrome" if z == s else "Not Palindrome"

print(rev, z)

