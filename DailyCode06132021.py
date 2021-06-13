# -----------------------------------------------------------
# #	Daily Code	06/13/2021
#   "May Check (v. 3)" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------------

# Check if it's May time. If not, then output =(

def mayCheck(text):
    strConvert = str(text)
    if strConvert == "May":
        return "TOTSUGEKI TOTSUGEKI TOTSUGEKI TOTSUGEKI"
    else:
        return "Welp, always next time =("

print mayCheck("May")
print mayCheck("Sol")