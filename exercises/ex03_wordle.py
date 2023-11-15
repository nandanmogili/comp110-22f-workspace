"""Wordle Project: Find a random word in 6 guesses!"""
__author__: str = "730573354"


def contains_char(answer: str, letter: str) -> bool:
    """When given two strings, searches first string for letter in second string, if it exists returns true, else it returns false."""
    assert len(letter) == 1  # ensures second string has a length of 1
    i: int = 0  # counter
    while i < len(answer):
        if answer[i] == letter[0]:
            return True
        i += 1
    return False  # if the letter is not found, function will return false


def emojified(guess: str, secret: str) -> str:
    """Takes 2 strings of equal length and returns a sequence of colored squares to show their relation."""
    assert len(guess) == len(secret)  # ensures the length of the guess and secret are the same
    j: int = 0  # counter
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while j < len(secret):  # loops 6 times
        if guess[j] == secret[j]:  # if the letter matches the letter of secret, a green box is added
            result += GREEN_BOX
        else:
            if contains_char(secret, guess[j]) is True:  # if true the letter exists yet its not in correct postion
                result += YELLOW_BOX
            else:  # if false this indicates that letter is not in secret
                result += WHITE_BOX
        j += 1
    return result


def input_guess(exlength: int) -> str:
    """Takes a integer for expected length, and then takes an string with that length."""
    guess: str = input(f"Enter a {exlength} character word: ")
    while len(guess) != exlength:
        guess = input(f"That wasn't {exlength} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    k: int = 1  # represents the turn counter
    secret = "party"  # sets the answer of the game to "codes"
    current_guess: str = " "
    while k <= 6 and current_guess != secret:
        print(f"=== Turn {k}/6 ===")
        current_guess = input_guess(5)
        print(emojified(current_guess, secret))
        if current_guess == secret:  # if the word is correct
            print(f"You won in {k}/6 turns!")
        elif k == 6 and current_guess != secret:
            print("X/6 - Sorry, try again tomorrow!") 
        k += 1


if __name__ == "__main__":
    main()