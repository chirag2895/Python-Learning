for i in range(1, 13):
    print("No. {0:2} square is {1:3} and cubed is {2:4}".format(i, i**2, i**3))  #{0:2} colon 2 is used to reserve space of 2 for the character

print()

for i in range(1, 13):
    print("No. {0:2} square is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3)) #{1:<3} <3 is used to align numbers, ^4 in {2:^4} used to centered the number

print()

print("Pi is approximately {0:12}".format(22/7)) #general format and defaults printing 15 decimals
print("Pi is approximately {0:12f}".format(22/7)) #assign floating function f to 12 we get the default of 6 digits after the decimal pont
print("Pi is approximately {0:12.50f}".format(22/7)) #still specifying floating format but also specifying precision of 50 after the decimal point
print("Pi is approximately {0:52.50f}".format(22/7)) #fit 50 values in 52 spaces
print("Pi is approximately {0:62.50f}".format(22/7)) #fit 50 values in 62 spaces
print("Pi is approximately {0:72.50f}".format(22/7)) #fit 50 values in 72 spaces

#use of f string
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")