# Lesson 12 - While Loops

# Recap 1: Multiples of 3 and 5
# Create a program to check if a number is both divisible by 3
# and 5.

# 1. Ask the user to input a number
# 2. Using the '%' operator, check if the number is both a
#    multiple of 3 and 5:
#     If true, print "The number is divisible by 3 and 5!"
# 3. Else, print "The number is not divisible by 3 and 5"

num = int(input("Key in a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by 3 and 5!")
else:
    print("The numberis no")
