day = "Monday"      #to get the output go swimming change day to saturday and rainig= False
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining:
    print("Go Swimming")
else:
    print("Learn Python")


if day == "Saturday" and temperature > 27 or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

#Both the output will be learn python but if you change day to saturday you will get output as learn python for and statement and go swimming for or statement
#if you change day to saturday and raining to false you will get both output as go swimming
#Suggestion: use Paranthesis when you use and or condition together in order to read easily