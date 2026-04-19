import random


numbers = [10, 20, 30, 40, 50]


chosen_number = random.choice(numbers)


guess = int(input("Guess the number: "))


if guess > chosen_number:
    print("Your guess is too high!")
elif guess < chosen_number:
    print("Your guess is too low!")
else:
    print(" You guessed it right!")
