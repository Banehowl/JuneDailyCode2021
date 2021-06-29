# --------------------------------------------------------------
# #	Daily Code	06/29/2021
#   "New Hobby of RC Drifting (Part 3)" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

def rcCheck(txt):
    if txt == "yes":
        return "Ordered the Sakura d5s v1"
    else:
        return "Aww but it's cool."

print rcCheck("yes")
print rcCheck("no")