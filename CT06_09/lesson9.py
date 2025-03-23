# import random
# a = random.randint(1,6)
# b = random.randint(1,6)
# c = random.randint(1,6)
# aIsEven = (a % 2) == 0
# bIsEven = (b % 2) == 0
# cIsEven = (c % 2) == 0
# AllIsSame = aIsEven == bIsEven == cIsEven
# print("First number:" + str(a))
# print("Second number:" + str(b))
# print("third number:" + str(c))

# print("All the numbers are even/odd:" + str(AllIsSame))



# import random

# a = random.randint(1,10)
# b = int(input("Guess the number from  1 to 10!"))
# if a == b:
#     print("So you were not dumb.")
# else:
#     print("Try again you failure.")

ApplesBought = int(input("How many apples do you want to buy?"))

if ApplesBought > 10 :
    ApplesBought = ApplesBought * 0.9
    print("You will get a 10% discount for that!The total cost of everything is:$" + str(ApplesBought))
else:
    print("The total cost of that is:$" + str(ApplesBought))