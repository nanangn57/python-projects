import random

print("Welcome to the guessing number game. You will  have to guess a random number from 1 to 100.")

play = 'y'
while play == 'y':
    GIVEN = random.randint(1, 100)
    level = input("What level do you want to play? type 'easy' or 'hard': ").lower()

    if level == 'easy':
        chances = 10
    else:
        chances = 5

    print(f"You have {chances} tries. Start guessing!")
    cont = True

    while cont:
        guess = int(input("What is your guess?"))
        if guess > GIVEN:
            chances -= 1
            print(f"Too high, you have {chances} chances left")
        elif guess < GIVEN:
            chances -= 1
            print(f"Too low, you have {chances} chances left")
        else:
            print(f"That's correct. You guess the right number when still have {chances} chances left.")
            cont = False
        if chances == 0:
            print(f"You have no chance left. The correct number is {GIVEN}")
            cont = False

    play = input("Do you want to continue guessing? type 'y' or 'n': ")
