import random 
import sys
# function's
def divider():
    print("----------------------------------------------------------------------")

name = "joe"
while True:

    if name == "joe":
        print("name is joe")
        break
print("thank you")


divider()



print("specific range")
for i in range(12 , 20):
    if(i == 15):
        continue
    print(i)


print("random range")
for i in range(12 , 20):
    if(i == 15):
        pass
    print(random.randint(12 , 20))


print("sys range")
for i in range(10):
    if(i == 5):
        sys.exit()
    print(random.randint(12 , 20))
