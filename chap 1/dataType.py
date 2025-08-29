def divider():
    print("----------------------------------------------------------------------")

int_vale = 3
float_val = 1.2
str_val = "hello string"
str_val1 = "crul world *o*"



# use first character
print(str_val[0])


# concating strings
print(str_val + str_val1)
divider()

# with whitespace
print(str_val + " " + str_val1)
# use f string
print(f"{str_val} {str_val1}")
divider()

# add str + number
# normally it gives an error of TypeError:
# print(str_val + int_vale)

# to use proper you have to conversion
print(str_val + str(int_vale))

divider()

# use mutltiple strings one liner
print(str_val * int_vale)
