# python-challenge-1
Week 2 assignment - menu, order and receipt

# Code Details
1. First, the higher level menu is displayed.
1. When user selects one of the menu number, the next level menu of items are displayed with prices.
1. When user selects a specific item, user is asked to enter quantity.
1. If quantity is not a number, quantity is defaulted to one.
1. The details of the user-selected item are fetched from the menu_items dictionary.
1. Each item is added as a dictionary to the order_list list.
1. If user enters an invalid number or any other character, an error message is displayed.
1. If user wants to keep ordering, the higher level menu is displayed again and all previous steps are rerun.
1. Once user stops ordering, the list of items ordered is displayed.
1. The final order total is also displayed.

# This is where I got the various sections of my code
* Menu printing code from the M2_Starter_Code package (lines 1-120)
* format() command syntax from a Google search (lines 187 onwards)
* List comprehension syntax from Week 3 Activity 10 (line 213)
