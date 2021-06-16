# -------------------------------------------------------------------------
# #	Daily Code	06/16/2021
#   "(One Line) Sum of Polygon Angles" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------------------

# Create a function that takes length and width and finds the perimeter of a rectangle.

# sum_polygon(3) -> 180
# sum_polygon(4) -> 360
# sum_polygon(6) -> 720

def sum_polygon(n):
    return (n - 2) * 180

print sum_polygon(3)
print sum_polygon(4)
print sum_polygon(6)
