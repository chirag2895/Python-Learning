answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print("You got it first time")

# Adding second guess
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")
# else:
#     print("You got it first time")


# Same but without using elif
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")