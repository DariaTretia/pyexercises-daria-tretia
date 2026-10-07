"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one sentence typed by the user, for example a product description copied
#    out of a supplier file.
# 2. Process: I apply four different text transformations to it, without changing
#    the original sentence.
# 3. Out: the original sentence plus four transformed versions, each one labelled.
# 4. My four transformations, and when each is useful:
#    - .strip()   : text copied out of an Excel export almost always arrives with
#                   spaces at both ends. This is the first thing to do before
#                   anything else, otherwise " Milan" and "Milan" look different.
#    - .title()   : to print a product name on a boutique shelf label, where every
#                   word starts with a capital.
#    - .upper()   : for the headline of a campaign banner or a press release.
#    - .replace() : to rename a collection everywhere at once, for example when
#                   "Pre-Fall" becomes "Autumn" in all the copy.
#    These four do genuinely different things: one cleans, one capitalises each
#    word, one capitalises everything, one swaps words.

# Your code below

sentence = input("Paste the product description: ")

print("Original     :", sentence)

# 1. Remove the spaces at the very start and the very end only.
cleaned = sentence.strip()
print("Cleaned      :", cleaned)

# 2. Capital on every word, the rest in lowercase.
as_label = cleaned.title()
print("Shelf label  :", as_label)

# 3. Everything in capitals.
as_headline = cleaned.upper()
print("Headline     :", as_headline)

# 4. Swap one word for another everywhere it appears.
renamed = cleaned.replace("Pre-Fall", "Autumn")
print("Renamed      :", renamed)

# The original is untouched: none of these methods change the sentence itself,
# they each hand back a NEW piece of text. That is why I stored each one in its
# own variable.
print("Original again:", sentence)

# CHECK IT YOURSELF - I ran it with "   Pre-Fall Silk Scarf in MILAN blue   "
# - Cleaned: the spaces at both ends are gone. Expected.
# - Shelf label: "Pre-Fall Silk Scarf In Milan Blue". NOT quite what I expected,
#   .title() also lowercased MILAN and put a capital on "In". Good to know before
#   I use it on a real label.
# - Headline: everything in capitals. Expected.
# - Renamed: "Autumn Silk Scarf in MILAN blue". Expected. Note it only worked
#   because I spelled "Pre-Fall" exactly, with the same capitals.
