# ---------------------------------------------
# #	Daily Code	06/18/2021
#   "Is it Hot Today? (Part 2)" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

def heatCheck(num):
    temperature = 80
    if num > temperature:
        return "HOT AS HELL"
    elif num == 80:
        return "On the borderline"
    else:
        return "Not bad TBH"

print heatCheck(70)
print heatCheck(80)
print heatCheck(90)