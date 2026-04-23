import random

jackpot = random.randint(1, 100)
counter = 1

print("------Number Guessing Game-----\n")
print("1 se 100 ke beech number guess karo")

while True:
    try:
        guess = int(input("Guess the Number: "))
    except ValueError:
        print(" Sirf number likho")
        continue

    if guess < 1 or guess > 100:
        print(" 1 se 100 ke beech likho")
        continue

    if guess < jackpot:
        print(" Guess Higher")
    elif guess > jackpot:
        print(" Guess Lower")
    else:
        print("--------Sahi Jawab--------")
        print(f"You took {counter} attempts")
        break

    counter += 1