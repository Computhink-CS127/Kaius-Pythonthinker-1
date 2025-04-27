# groceries=[
# "Apples",
# "Bread",
# "Carrots",
# "Dates",
# "Eggs",
# "Flour",
# "Grapes",
# "Honey"]
# groceries[7]="Herbs"
# groceries.append("Ice")
# groceries.insert(1,"Bananas")
# groceries.pop(2)
# for grocery in groceries:
#     if grocery == "Apples":
#         print("I need 5 of these.")
#     elif grocery == "Carrots":
#         print("I need 3 of these.")
#     elif grocery == Grapes:
#         print("Get the Farmfresh brand.")


# Task 2: List of groceries (part 2)
# 1. Use a 'for' loop and print out all the groceries on your list
# 2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
# 3. If grocery == "Carrots", print "<grocery name>: I need 3 of
#    these"
# 4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
#    brand"

# Task 4: Online Catalogue
# **Task 4a**:
# Write a program to create an online catalogue for a grocery store.

# 1. Using a 'while' loop, ask the user (grocery store manager) to
#    input the items their online catalogue should have.
# 3. Add each item into the catalogue list
# 4. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the grocery store manager, do the
# following:

# 1. Imagine a customer browsing the website of the grocery store.
#    Ask the customer: "What are you looking for?"
# 2. If the item is in the list, say "Yes we sell that."
# 3. Else, say "Sorry, we don't have that."
catalogue = []
while True:
    AddItem = input("What item do you want?")
    if AddItem == "end":
        break
    else:
        catalogue.append(AddItem)

ItemWanted = input("What do you want?")

if ItemWanted in catalogue:
    print("Yes,we sell that.")
else:
    print("Sorry,we don't have that.")



