# ---------------------------------------------
# #	Daily Code	06/18/2021
#   "Is it Hot Today?" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

def heatCheck(num):
    temperature = 80
    if num > temperature:
        return "HOT AS HELL"
    else:
        return "Not bad TBH"

print heatCheck(70)
print heatCheck(90)