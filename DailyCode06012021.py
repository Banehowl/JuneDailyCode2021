# ---------------------------------------------------------------------------
# #	Daily Code	06/01/2021
#   "(One Line) Return the Remainder of Two Numbers" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------------------

# There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are
# passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero.
# Return that value.

# remainder(1, 3) -> 1
# remainder(3, 4) -> 3
# remainder(5, 5) -> 0
# remainder(7, 2) -> 1

def remainder(x, y):
    return x % y

print remainder(1, 3)
print remainder(3, 4)
print remainder(5, 5)
print remainder(7, 2)