"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing is typed by the user. The only thing that goes in is a number
#    I write myself in the code: how many times the message must appear.
# 2. Process: the program counts from 1 up to that number, and for each count it
#    prints the line number followed by my message.
# 3. Out: five numbered lines in the terminal, all with the same message.
# 4. My message, and why: "Check the stock before you promise a delivery date."
#    I chose it because in a boutique the mistake that costs the most is promising
#    a piece to a client when it is not actually in stock. "Hello, World!" tells
#    nobody anything. A program that repeats a rule is at least a reminder.

# Your code below

# The number of lines is stored in a variable, not written five times.
# If I want 3 lines instead of 5, I change the 5 below and nothing else.
number_of_lines = 5

message = "Check the stock before you promise a delivery date."

# range(1, 6) gives 1, 2, 3, 4, 5. The second number is not included,
# so I have to write number_of_lines + 1 to really get 5 lines.
for line_number in range(1, number_of_lines + 1):
    print(line_number, "-", message)

# I checked: I counted 5 lines in the terminal.
# Then I put 3 instead of 5 and I got exactly 3 lines, one character changed.
