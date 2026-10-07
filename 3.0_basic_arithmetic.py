"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two numbers typed by the user. In my case: the retail price of a piece,
#    and the number of pieces received in the boutique.
# 2. Process: the two answers arrive as text, I turn them into numbers, then I
#    apply the four operations to them.
# 3. Out: the four results, each one labelled, and a clear message instead of a
#    result when the second number is zero.
# 4. What happens when the second number is zero, and why: I display a message
#    instead of a result, and the program carries on to the end.
#    I did not choose to crash, because a program that stops in the middle of a
#    stock report loses everything it had already computed. I did not choose to
#    ask again either, because at this stage I have no loop and the user might
#    type zero for ever. Printing "division by zero is not possible" keeps the
#    three other results visible, which is the useful behaviour.

# Your code below

price_text = input("Retail price of the piece, in euros: ")
quantity_text = input("How many pieces were received? ")

price = int(price_text)
quantity = int(quantity_text)

print("Sum       :", price + quantity)
print("Difference:", price - quantity)
print("Product   :", price * quantity)

# Division is the only one that can fail, so it is the only one I protect.
if quantity == 0:
    print("Division  : not possible, I cannot divide by zero.")
else:
    print("Division  :", price / quantity)
    print("Whole part of the division:", price // quantity)

# CHECK IT YOURSELF
# I worked out 7 divided by 2 in my head: 3.5.
# With 7 and 2 my program shows 3.5 on the "Division" line, and 3 on the line
# below. The reason is that Python has TWO divisions:
#   /  gives the exact result, with the decimals: 3.5
#   // throws the decimals away and keeps only the whole part: 3
# So a program showing 3 is not broken, it was asked the wrong question. In a
# stock context // is actually the right one: I cannot sell half a handbag.
# With 0 as the second number I get my message and the program still finishes.
