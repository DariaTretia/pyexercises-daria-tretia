"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the budget list from exercise 4.0, written again here so this file runs
#    on its own.
# 2. Process: I produce four different orders of it. Two of them are built on a
#    COPY, so the original survives; the two that modify in place are applied to
#    a copy on purpose.
# 3. Out: the four orders, then the original list printed last to prove it has
#    not moved.
# 4. My four orders, and which ones modify the original:
#    - sorted(list)               -> smallest budget first. Returns a NEW list.
#                                    The original is NOT touched.
#    - sorted(list, reverse=True) -> biggest budget first. Also a NEW list.
#                                    The original is NOT touched.
#    - list[::-1]                 -> the list read backwards. Also a NEW list.
#                                    The original is NOT touched.
#    - copy.sort()                -> sorts IN PLACE and returns nothing. This one
#                                    DOES modify the list it is called on, which
#                                    is why I call it on a copy and never on the
#                                    original.
#    The whole point: sorted() and [::-1] build something new, .sort() and
#    .reverse() change the thing itself. If I had written
#    monthly_budget_keur.sort() I would have destroyed the original order of 4.0
#    without any error message.

# Your code below

boutique_cities = ["Paris", "Milan", "London", "Dubai", "Tokyo", "Seoul", "New York", "Shanghai"]
monthly_budget_keur = [180, 140, 155, 210, 165, 120, 230, 195]

print("Original order :", monthly_budget_keur)

# Order 1 - new list, smallest first.
print("1. Ascending   :", sorted(monthly_budget_keur))

# Order 2 - new list, biggest first.
print("2. Descending  :", sorted(monthly_budget_keur, reverse=True))

# Order 3 - new list, same values read from the end to the start.
print("3. Backwards   :", monthly_budget_keur[::-1])

# Order 4 - this one modifies, so I work on a copy.
# .copy() gives me a separate list. Without it, working_list and
# monthly_budget_keur would be two names for the SAME list, and sorting one
# would silently sort the other.
working_list = monthly_budget_keur.copy()
working_list.sort()
print("4. Sorted copy :", working_list)

# Proof, as the last line of the program.
print("Original, untouched:", monthly_budget_keur)

# CHECK IT YOURSELF
# I compared item by item with 4.0: 180, 140, 155, 210, 165, 120, 230, 195.
# Same values, same order. Nothing moved.
