"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the two lists from exercise 4.0, copied across: the eight flagship cities
#    and their monthly media budget in thousands of euros.
# 2. Process: for every city I compute its share of the total budget as a
#    percentage, and I compare it to the average to flag it.
# 3. Out: one line per city, with its position in the list, its name, its budget,
#    its share of the total, and whether it is above or below the average.
# 4. What I compute for each item, and why it is worth showing: the share of the
#    total. A raw budget means nothing on its own, 180 is only big or small next
#    to what the others get. The share turns eight numbers into a split, and the
#    above/below average flag is what makes the line readable in one second
#    during a meeting. That is the whole point of the line.

# Your code below

boutique_cities = ["Paris", "Milan", "London", "Dubai", "Tokyo", "Seoul", "New York", "Shanghai"]
monthly_budget_keur = [180, 140, 155, 210, 165, 120, 230, 195]

total_budget = sum(monthly_budget_keur)
average_budget = total_budget / len(monthly_budget_keur)

print("Total:", total_budget, "kEUR - average per city:", round(average_budget, 1), "kEUR")
print("")

# range(len(...)) gives me 0, 1, 2, ... 7, which are exactly the positions that
# exist in BOTH lists. That is how I keep the city and its budget together.
for position in range(len(boutique_cities)):
    city = boutique_cities[position]
    budget = monthly_budget_keur[position]

    # Share of the total, rounded to one decimal so the line stays readable.
    share = round(budget / total_budget * 100, 1)

    # My threshold is the average. Above it, the city is flagged.
    if budget > average_budget:
        flag = "above average"
    else:
        flag = "below average"

    print(position + 1, "-", city, ":", budget, "kEUR,", share, "% of total,", flag)

# CHECK IT YOURSELF
# I counted the printed lines: 8, and my list has 8 cities. No off-by-one.
# The reason there is no off-by-one is that range(len(list)) stops on its own at
# the last real position. If I had written range(1, 9) and used it as an index,
# the last city would have crashed the program.
# Quick check by hand: Paris is 180 out of 1395, which is 12.9 per cent.
# The program agrees.
