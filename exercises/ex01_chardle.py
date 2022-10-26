"""Chardle Program - Finds Letters in Words!"""
__author__ = "730573354"

index: int = 0
instances: int = 0

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + str(letter) + " in " + word)

if word[index] == letter:  # Checks letter at index 0
    print(letter + " found at index " + str(index))
    index += 1
    instances += 1
else:
    index += 1

if word[index] == letter:  # Checks letter at index 1
    print(letter + " found at index " + str(index))
    index += 1
    instances += 1
else:
    index += 1

if word[index] == letter:  # Checks letter at index 2
    print(letter + " found at index " + str(index))
    index += 1
    instances += 1
else:
    index += 1

if word[index] == letter:  # Checks letter at index 3
    print(letter + " found at index " + str(index))
    index += 1
    instances += 1
else:
    index += 1

if word[index] == letter:  # Checks letter at index 4
    print(letter + " found at index " + str(index))
    index += 1
    instances += 1
else:
    index += 1
# prints number of instances in the word
if instances == 0:
    print("No instances of " + letter + " found in " + word)
if instances == 1:
    print(str(instances) + " instance of " + letter + " found in " + word)
else:
    print(str(instances) + " instances of " + letter + " found in " + word)