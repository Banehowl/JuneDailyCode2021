# --------------------------------------------------------------------
# #	Daily Code	06/06/2021
#   "(One Line) Maximum Edge of a Triangle" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------------

# Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

# next_edge(8, 10) -> 17
# next_edge(5, 7) -> 11
# next_edge(9, 2) -> 10

def next_edge(x, y):
    return (x + y) - 1

print next_edge(8, 10)
print next_edge(5, 7)
print next_edge(9, 2)