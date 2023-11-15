"""A"""
__author__ = "730559172"


secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
colors: str = ""
counter = 0
counter2 = 0

if int(len(guess)) != 6:
    print("That was not 6 letters! Try again:")
    guess = str(input("What is your 6-letter guess? "))
if guess == secret_word:
    while (counter < 6):
        colors = colors + GREEN_BOX  
        counter += 1
    print(colors)
    print("Woo! You got it!")

if guess != secret_word:
    while (counter < len(secret_word)):
        if guess[counter] == secret_word[counter]:
            colors = colors + GREEN_BOX
        else:
            counter2 = 0
            playing_tem = False
            while(playing_tem is False and counter2 < 6):
                if guess[counter] == secret_word[counter2]:
                    colors = colors + YELLOW_BOX
                    playing_tem is True
                else:
                    counter2 += 1
                if playing_tem is False and playing_tem == len(secret_word):
                    colors = colors + WHITE_BOX
        counter += 1
    print(colors)
    print("Not quite. Play again soon!")