
#Task 1
# Print numbers from 10 to 200 using the while loop
# Your numbers must be in multiples of 10.
# 10 must be first number printed, and 200 the last number.

# Example: 10, 20, 30 ..... 180, 190, 200.
# Note that the numbers do not need to be printed in one line.
# Write your code here
num = 0
while num < 200:
    num = num + 10
    print(num)
fal



###################################################

# Task 2
# Code a password checker to protect your code!

# Assign a password "superpass123" to a variable
# Ask the user to enter a password
# If the password matches, print “Access Granted”
# If the password does not match, print “Access Denied”

# Write your code here
password = "superpass123"

UserGuess = input("Guess the password! ")
while True:
    if UserGuess == password:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        UserGuess = input("Guess the password!")
        
