"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing typed by the user. One product record written in the code.
# 2. Process: I read one field, I change one field, I remove one field, then I go
#    through everything that is left and display it.
# 3. Out: the product record printed field by field, before and after my changes.
# 4. My object, my five fields, and why those: I described one product reference,
#    a silk scarf from the current collection, the way it appears in a boutique
#    stock sheet. My fields:
#    - reference    : the only field that is truly unique. Two scarves can share a
#                     name, never a reference. This is what a stock system keys on.
#    - name         : what the client and the sales assistant actually say.
#    - category     : how the piece is grouped in a report (silk, leather goods).
#    - retail_price : needed for every single sales computation.
#    - stock_paris  : how many are physically in the Paris boutique right now.
#                     This is the field that decides whether I can promise a piece.
#    I added season because a scarf that is two seasons old is managed differently
#    from a new one, and it is the field I remove later as a demonstration.

# Your code below

# A dictionary stores pairs: a key on the left, its value on the right.
# Unlike a list, I find things by name rather than by position.
silk_scarf = {
    "reference": "SC-4412-BLU",
    "name": "Carre Milano 90",
    "category": "Silk",
    "retail_price_eur": 480,
    "stock_paris": 12,
    "season": "Pre-Fall 2026",
}

# Reading one field, by its name.
print("Reference:", silk_scarf["reference"])
print("Price    :", silk_scarf["retail_price_eur"], "EUR")

# Changing a field. Three pieces sold today, so the Paris stock goes down.
silk_scarf["stock_paris"] = silk_scarf["stock_paris"] - 3
print("Stock in Paris after the sales of the day:", silk_scarf["stock_paris"])

# Removing a field. The season stops being relevant once the piece moves to the
# permanent collection, so the field goes away entirely.
del silk_scarf["season"]

# Displaying every field with its value.
# .items() hands me the key AND the value on each turn of the loop.
print("Full product record:")
for field_name, field_value in silk_scarf.items():
    print(" -", field_name, ":", field_value)

# CHECK IT YOURSELF - asking for a field that does not exist.
# I first wrote print(silk_scarf["colour"]) and the program CRASHED with
# KeyError: 'colour'. A dictionary does not invent a missing field, it stops.
# .get() is the version that survives: it hands back None, or whatever default
# I give it as a second argument, instead of crashing.
print("Colour (missing field, with .get):", silk_scarf.get("colour", "not recorded"))
print("Season (just deleted, with .get):", silk_scarf.get("season", "not recorded"))
