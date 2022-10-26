"""Demonstrates asking the user for input."""
# Input function call has priority so it asks question takes input and prints result
user_name : str = input("What is your name? ")
print("Hello " + user_name + ", good morning! " )
print("You are awesome, " + user_name)
age: int = 21
msg: str = f"You are {age}!"
print(msg)