# op's to use
# == equalTo
# != Not EqualTo
# < Less Than
# > Greater Than
# <= LessThen EqualsTo
# >= Greater Tan Equals To

# function's
def divider():
    print("----------------------------------------------------------------------")


# variable's
age = 18
HasVoterCard = True
code = 1111


price = 8000

# condition's
if(price != 8000):
    print("price is greater then 8000 ")
else:
    print("not equals to 8000")

divider()

if(code == 1111):
    print("you enter'd right code !")
    if(age >= 18):
        print("eligible for driving ")
        if(HasVoterCard):
            print("user has votter card")
    else:
        print("you are not eligible for driving")
else:
    print("Code didn't match")

# note: uses
# equals to and greater equals to 


divider()

if(HasVoterCard and price >= 8000):
    print("has voter card but not 8000 price")
elif(HasVoterCard and price == 8000):
    print("has votter card but has 8000 price")
else:
    print("not has anything")


divider()

print("Enter TB or GB for the advertised unit:")
unit = input('>')

if unit == "TB" or unit =='tb':
    discrepancy = 10000000000 / 1099511627776
elif unit == "GB" or unit == 'gb':
    discrepancy = 10000000000 /1073741824

print("enter the advertised capacity")
advertised_Capacity = input(">")
advertised_Capacity = float(advertised_Capacity)
real_capacity = str(round(advertised_Capacity * discrepancy , 2))
print("actual capacity is" + real_capacity + "unit")



