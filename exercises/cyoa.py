"""Choose Your Own Adventure Game (Dating Simulator)!"""
__author__: str = "730573354"
from random import randint
points: int
player: str
LOVEFACE = "\U0001F970"
HEARTEYES = "\U0001F60D"


def main() -> None:
    """Main Function that is run as a module."""
    global points
    global player
    global HEARTEYES
    global LOVEFACE
    points = 0
    i: int = 0

    greet()  # prints instructions and takes the users name
    print(f"You just met the future love of your life, Kris. {HEARTEYES}{LOVEFACE}{HEARTEYES}")
    print(f"This is your chance {player}, to finally find love. {LOVEFACE}{LOVEFACE}{LOVEFACE}")
    print("Make your move before its too late!")

    while i < 10:  # runs the game loop 10 times
        print(f"\nTurn {i+1}/10\n")
        game()
        i += 1
    
    if points >= 45:
        print(f"\nCongratulations {player} your smooth moves got you {points} attraction points.{LOVEFACE}{LOVEFACE}{LOVEFACE}")
        print(f"You found true love!!!{HEARTEYES}{LOVEFACE}{HEARTEYES}\n")
    else:
        print(f"\nUnfortunately you only obtained {points} points.")
        print("There are plenty of fish in the sea, try again next time.\n")


def greet() -> None:
    """Greets the user and prompts them for their name."""
    global LOVEFACE
    global HEARTEYES
    global player
    print(f"Welcome to Dating Simulator, A game where you test your luck at Love!{LOVEFACE}{HEARTEYES}")
    print("Make decisions that affect your chance at a relationship.")
    print("If you obtain atleast 45 attraction points before turn 10 you will find love.")
    player = input("Enter Name of Player: ")


def safe_move() -> None:  # procedure
    """If the user makes a safe move it could have a small but positive change in attraction."""
    global points
    num: int = 2
    change: int = randomizer(num)
    pos_or_neg_var: int = randint(1, 8)
    phrase_var: int = randint(1, 2)
    if pos_or_neg_var % 8 == 0:  # 1/8 odds to be negative
        change *= -1
    if change > 0:
        if phrase_var == 1:
            print('\nKris: "Thats very nice of you."')
        if phrase_var == 2:
            print('\nKris: "Thats sweet."')
    else:
        if phrase_var == 1:
            print('\nKris: "What do you mean by that?"')
        if phrase_var == 2:
            print('\nKris: "Moving on..."')
    points += change


def risky_move() -> None:  # procedure
    """If the user makes a risky move it could have a large positive or negative change in attraction."""
    global points
    global LOVEFACE
    global HEARTEYES
    num: int = 1
    change: int = randomizer(num)
    pos_or_neg_var: int = randint(1, 3) 
    phrase_var: int = randint(1, 2)
    if pos_or_neg_var % 3 == 0:  # 1/3 odds to be negative
        change *= -1
    if change > 0:
        if phrase_var == 1:
            print(f'\nKris: "Wow your so nice!" {LOVEFACE}{HEARTEYES}')
        if phrase_var == 2:
            print(f'\nKris: "I think im into you!" {LOVEFACE}{HEARTEYES}')
    else:
        if phrase_var == 1:
            print('\nKris: "Eww why would you say that."')
        if phrase_var == 2:
            print('\nKris: "I cant look at you the same after that."')
    points += change


def small_talk() -> None:  # procedure
    """If the user decides to small talk it has no risk but only a slight positive change in attraction."""
    global points
    num: int = 3
    change: int = randomizer(num)
    phrase_var: int = randint(1, 2)
    points += change
    if phrase_var == 1:
        print('\nKris: "Thats so cool to hear."')
    if phrase_var == 2:
        print('\nKris: "Yeah the weather is great!"')


def randomizer(num: int) -> int:  # function
    """Finds the neccesary odds based on which decision is chosen."""
    result: int = 0
    if num == 1:
        result = randint(9, 16)
        return result 
    elif num == 2:
        result = randint(5, 9)
        return result
    elif num == 3:
        result = randint(3, 5)
        return result


def game() -> None:
    """Game Cycle, this is looped 10 times."""
    global player
    global points
    print("----------------- Options --------------------")
    print("1. Flirt Aggressively (High Risk, High Reward)")
    print("2. Flirt Passively (Low Risk, Low Reward)")
    print("3. Make Small Talk (No risk, Small Reward)")
    print("----------------------------------------------")
    choice: int = 0
    choice = int(input("Choose the number that corresponds to the selected choice: "))
    print("\n\n")

    if choice == 1:
        risky_move()
    elif choice == 2:
        safe_move()
    elif choice == 3:
        small_talk()
    else:
        print("error: improper input ")
    
    print(f"{player}, Kris's current attraction to you is {points}")


if __name__ == "__main__":
    main()