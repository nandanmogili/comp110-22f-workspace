"""Examples of using lists in a simple "game" ."""

from random import randint
rolls: list[int] = list() #  makes an empty list

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1,6))

print(rolls)



# remove an item from the list by its index (pop)
rolls.pop(len(rolls)-1)
print(rolls)

# sum the values of our rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum += rolls[i]
    i += 1
print(f"Total Score: {sum}")


# rolls.append(randint(1,6)) # appends a object to the end of the list 
# rolls.append(randint(1,6))

# print(rolls)


# # access an individual value in the list
# print(rolls[0])
# print(rolls[1])

# print(len(rolls))
