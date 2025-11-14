import random

random_num = random.randint(1, 10)
guess = int(input("Whats your guess? "))

while guess != random_num:
    if guess > random_num:
        print("The number is smaller!")
    elif guess < random_num:
        print("The number is bigger!")

    guess = int(input("Whats your guess? "))

print(f'Correct! The number was {random_num}')
