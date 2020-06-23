age = 24
print("My age is " + str(age) + " years")  # Using + operator to add integer in to a string using str function
# Using dot format
print('My age is {0} years'.format(age)) # gives the same output as line 2

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec")) #shows that we can have multiple replacement fields inside a string
#In this code, we used 8 replacement fields- numbere from 0 to 7, These are replaced with the values in the parantheses after .format, the first value goes into {0}, the second in {1}, and so on.

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))
print()
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))
