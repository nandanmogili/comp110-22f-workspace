"""One Shot Wordle."""
__author__: str = "730573354"

answer: str = "python"
result: str = " "
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0  # First variable which loops through every letter in the guess


guess: str = input("What is your 6-letter guess? ")  # validates the input to have correct number of letters
while len(guess) != len(answer):
    guess = input("That was not 6 letters! Try again: ")


while i < len(answer):
    if guess[i] == answer[i]:
        result += GREEN_BOX
    else:
        bol: bool = False  # boolean variable that starts false
        j: int = 0  # this is the second variable which is used to check whether the letter is in the answer but wrong index
        while j < len(answer):
            if guess[i] == answer[j]:  # if letter exists in the answer boolean switches yo true
                bol = True
            j += 1
        if bol is True:  # if true adds a yellow box
            result += YELLOW_BOX
        else:  # if false adds a white box
            result += WHITE_BOX
    i += 1
print(result)  # prints the boxes 

if guess == answer:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
