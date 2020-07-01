name = input("Hello, What's your name? ")
age = int(input("What's your age? "))

if 18 <= age < 31:
    print("{}, Welcome to the Holiday Club".format(name))
else:
    print("Sorry, {} you cannot enter Holiday Club".format(name))
