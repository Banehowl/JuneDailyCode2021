# -----------------------------------------------------
# #	Daily Code	06/27/2021
#   "New Hobby of RC Drifting" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------

def rcCheck(txt):
    if txt == "yes":
        return "NICE! Let's go!"
    else:
        return "Aww but it's cool."

print rcCheck("yes")
print rcCheck("no")