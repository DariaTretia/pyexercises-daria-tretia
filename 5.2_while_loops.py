"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: answers typed by the user, as many times as needed. I ask which flagship
#    city they want the budget for.
# 2. Process: the program keeps asking until the user names a city that is really
#    in my list, or until they have used up their attempts. Every answer is
#    cleaned up before it is compared.
# 3. Out: the budget of the city if it was found, and in every case a summary of
#    what happened during the loop: how many attempts were used, what was typed,
#    and how it ended.
# 4. My stop condition, my attempt limit, my summary:
#    - Stop condition: the cleaned answer matches one of my eight cities. The user
#      can also type quit to leave on purpose, because forcing someone to answer
#      correctly in order to escape a program is bad design.
#    - Attempt limit: 4. After four wrong answers the problem is not the typing,
#      it is that the city is not in the list, and asking a fifth time will not
#      change that. Without this limit the loop could run for ever.
#    - Summary: the number of attempts used, every answer that was typed, and the
#      outcome: found, gave up, or limit reached.
#    I also decided that paris, PARIS and "  Paris  " are the same answer.
#    A sales assistant typing in a hurry should not be punished for a capital.

# Your code below

boutique_cities = ["Paris", "Milan", "London", "Dubai", "Tokyo", "Seoul", "New York", "Shanghai"]
monthly_budget_keur = [180, 140, 155, 210, 165, 120, 230, 195]

# The same list in lowercase, so I can compare without worrying about capitals.
cities_lowercase = []
for city in boutique_cities:
    cities_lowercase.append(city.lower())

max_attempts = 4
attempts_used = 0
answers_given = []
outcome = "limit reached"

while attempts_used < max_attempts:
    answer = input("Which flagship city? (type quit to stop) ")
    attempts_used = attempts_used + 1

    # .strip() removes the spaces at both ends, .lower() removes the capitals.
    # This is the line that makes "  PARIS " and "Paris" the same answer.
    cleaned = answer.strip().lower()
    answers_given.append(cleaned)

    if cleaned == "quit":
        outcome = "the user gave up"
        break

    if cleaned in cities_lowercase:
        # .index() gives me the position of the city, and that same position
        # points at its budget in the other list.
        position = cities_lowercase.index(cleaned)
        print("Monthly budget for", boutique_cities[position], ":", monthly_budget_keur[position], "kEUR")
        outcome = "city found"
        break

    print("Not a flagship city. Attempts left:", max_attempts - attempts_used)

# The summary, printed whatever happened.
print("")
print("--- Summary ---")
print("Attempts used:", attempts_used, "out of", max_attempts)
print("What was typed:", answers_given)
print("Outcome:", outcome)

# CHECK IT YOURSELF
# I ran it and never gave a real city: it stopped on its own after 4 attempts and
# printed the summary with "limit reached". It did not run for ever.
# I ran it again with "  MILAN  " and it was accepted straight away, because of
# the .strip().lower() line.
