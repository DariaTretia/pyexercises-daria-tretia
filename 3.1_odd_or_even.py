"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number N typed by the user. For me it is the number of seats to
#    prepare along a runway.
# 2. Process: the program goes through every number from 1 to N and tests whether
#    it can be divided by 2 with nothing left over.
# 3. Out: one line per seat saying odd or even, which is how I know which side of
#    the runway the seat goes on. Odd on the left, even on the right.
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0        : I print "no seat to prepare" and stop there. Zero is a legitimate
#                 answer (the show is cancelled), it is not an error.
#    - negative : I refuse it with a message. A negative number of seats does not
#                 exist, and printing nothing silently would make the user think
#                 the program is broken.
#    - over 100 : I refuse it with a message too. Nobody reads five thousand lines
#                 in a terminal. 100 is my limit and it is a decision, not a law:
#                 above that this should be written to a file, not printed.

# Your code below

seats_text = input("How many seats do we prepare? ")
seats = int(seats_text)

# The three decisions above, in the same order, before any loop starts.
if seats < 0:
    print("A negative number of seats does not exist. Nothing done.")
elif seats == 0:
    print("No seat to prepare.")
elif seats > 100:
    print("Over 100 seats, this does not belong in a terminal. Nothing printed.")
else:
    # range(1, seats + 1) counts 1, 2, ... up to seats included.
    for seat_number in range(1, seats + 1):
        # % is the remainder of the division. If dividing by 2 leaves 0, the
        # number is even. There is no other case: the remainder is 0 or 1.
        if seat_number % 2 == 0:
            print("Seat", seat_number, ": even  -> right side")
        else:
            print("Seat", seat_number, ": odd   -> left side")

# CHECK IT YOURSELF
# With 6 I counted the lines: seats 1, 3, 5 are odd and 2, 4, 6 are even.
# Three of each, which is what was expected.
# With 0, with -4 and with 5000 I got my three messages and no list.
