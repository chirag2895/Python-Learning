a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print()

for i in range(1,4):
    print(i)

#or
for i in range(1, a//b):
    print(i)

#use of operators precedence

print(a + b /3 - 4 * 12)
# because python uses PEDMAS
print(a + (b / 3)- (4 * 12))
# but if you want to go in a flow then
print((((a + b) / 3) - 4) * 12)
#or
print(((a + b) /3 -4) * 12)
