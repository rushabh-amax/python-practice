import random

# function's
def divider():
    print("----------------------------------------------------------------------")
# while
spam  = 0
while spam < 5:
    print("hellow")
    spam = spam + 1
    print("how spam increae" , spam)


# syntax:
# keywork condition:
#     code
#     inc/dic


# range[]

divider()

print("used range here")
for i in range(5):
    print(i)

divider()

print("used range for sum")
sum = 0
for i in range(10):
    sum = sum + i
    print(sum)


print("specific range")
for i in range(12 , 20):
    print(i)

print("random range")
for i in range(12 , 20):
    print(random.randint(12 , 20))