import random


def play_game():
    secret_number = random.randint(1, 1000)
    turns = 0
    while True:
        guess = int(input("Guess the number 1-1000: "))
        if turns == 9:
            print("That's enough, better luck next time")
            break
        if guess == secret_number:
            print("Jackpot, you guessed the number")
            break
        elif guess < secret_number:
            print("To low")
            turns += 1
        elif guess > secret_number:
            print("To high")
            turns += 1
    print("Number of turns = ", turns + 1)


while True:
    play_game()

    play_again = input("Do you want to play again? (y/n) ").strip().lower()
    if play_again not in "y":
        print("Goodbye")
        break
