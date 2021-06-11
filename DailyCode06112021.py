# -----------------------------------------------------------
# #	Daily Code	06/11/2021
#   "May Check" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------------

# Check if it's May time. If not, then output =(

def mayCheck(text):
    strConvert = str(text)
    if strConvert == "May":
        return "TOTSUGEKI"
    else:
        return "=("

print mayCheck("May")
print mayCheck("Sol")
