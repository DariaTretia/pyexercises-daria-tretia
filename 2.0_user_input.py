"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two things typed by the user: the city of the boutique they are calling
#    from, and the amount in euros the client spent with us last year.
# 2. Process: the city stays text, the amount has to become a number before I can
#    do anything with it. Then I build one sentence with both.
# 3. Out: one sentence that says which boutique, which client spend, and which
#    client tier that spend puts them in.
# 4. My two fields, and what I would do with them: this is the clienteling form a
#    sales assistant fills in after a call. The city tells me which boutique owns
#    the relationship, the annual spend decides whether the client gets invited to
#    the private sale. Those two fields alone already drive a real decision, which
#    is why I did not pick "name and age".

# Your code below

boutique_city = input("Which boutique are you calling from? ")
annual_spend_text = input("How much did the client spend last year, in euros? ")

# input() ALWAYS gives back text, even when the user types 4500.
# If I try annual_spend_text + 1 here, Python stops with a TypeError, because it
# refuses to add a number to a piece of text. So I convert it first with int().
annual_spend = int(annual_spend_text)

# Now that it is a real number I can actually compute with it.
next_year_target = annual_spend + 1000

print("Client file:", boutique_city, "boutique, spend last year:", annual_spend, "EUR.")
print("Target for next year:", next_year_target, "EUR.")

# CHECK IT YOURSELF - what happened when I tested the bad answers:
# - Empty line for the city: the program carried on and printed an empty space in
#   the sentence. It did not crash, but the sentence made no sense.
# - A single space for the city: same thing, Python treats " " as a real answer.
# - Text where I expected a number ("a lot"): the program CRASHED on the int()
#   line, with ValueError: invalid literal for int() with base 10: 'a lot'.
#   So int() is the line that is fragile, not input().
