#        012345678901234
parrot= "Norwegian Blue"

print(parrot[0:6])  #start from 0 and extends upto but not including index position 6, this will give Norweg
print(parrot[3:5])  # starts from 3 and extend upto but not including 5
print(parrot[0:9])
print(parrot[:9])  #same as line 6
# if want to print Blue
print(parrot[10:14])
print(parrot[10:]) #same as line 9
print()
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])  #start from the beginning and stop till the end


# Negative Slicing
print(parrot[-4:-2])
print(parrot[-4:12])
print(parrot[-14:-8])   #same as line 4

# Using step in sclicing
print(parrot[0:6:2])  #the sclice starts at index postion 0, it extends upto but not including position 6, we step through the sequence in steps of 2
print(parrot[0:6:3])

print(parrot[1::4])  #starts with position 1 and slice every 4 character

#Slicing Backwards
letters='abcdefghijklmnopqrstuvwxyz'
backwards = letters[25:0:-1]
print(backwards)
