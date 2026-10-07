"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. The data is written in the code: the eight
#    cities where the brand has a flagship boutique, and the monthly media budget
#    allocated to each of them, in thousands of euros.
# 2. Process: I display the list, I pick one city out of it, I sort the budgets,
#    and I compute the total and the average of the budgets.
# 3. Out: the full list, one chosen item, the sorted budgets, and two computed
#    numbers: the total monthly budget and the average per city.
# 4. What my list is about, and what I computed from it: it is the monthly media
#    budget per flagship city. I computed the total, because that is the number
#    the finance team asks for, and the average per city, because that is the line
#    every city is compared against. A city under the average is either a small
#    market or a city we are under-investing in, and that is the conversation the
#    number is supposed to start.

# Your code below

# The two lists go together, position by position:
# boutique_cities[0] is Paris, and its budget is monthly_budget_keur[0] = 180.
boutique_cities = ["Paris", "Milan", "London", "Dubai", "Tokyo", "Seoul", "New York", "Shanghai"]
monthly_budget_keur = [180, 140, 155, 210, 165, 120, 230, 195]

print("All flagship cities:", boutique_cities)
print("All monthly budgets (kEUR):", monthly_budget_keur)

# One item of my choice. Positions start at 0, so [3] is the FOURTH city, Dubai.
print("The city in position 3 is:", boutique_cities[3])
print("Its monthly budget is:", monthly_budget_keur[3], "kEUR")

# sorted() hands back a NEW sorted list and leaves the original alone.
print("Budgets sorted, smallest first:", sorted(monthly_budget_keur))

# Something computed from the list.
total_budget = sum(monthly_budget_keur)
average_budget = total_budget / len(monthly_budget_keur)

print("Total monthly budget:", total_budget, "kEUR")
print("Average per city:", average_budget, "kEUR")
print("Highest budget:", max(monthly_budget_keur), "kEUR")

# CHECK IT YOURSELF
# By hand on my first three cities: 180 + 140 + 155 = 475.
# I checked with sum(monthly_budget_keur[0:3]) and Python also says 475.
print("Check on the first three cities:", sum(monthly_budget_keur[0:3]))
