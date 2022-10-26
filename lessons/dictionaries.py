"""Demonstrating some of dictionaries capabilities."""

# declaring a type of dictionary
schools: dict[str, int]

#initialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dicitionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
#print(schools)  # output: {'UNC': 19400, 'Duke': 6717, 'NCSU': 26150}

# Access a value by its key (look up)
#print(f"UNC has {schools['UNC']} students")

# popping a value from a dictionary
schools.pop("Duke")

# Test for the existence of a key (checks if "Duke" is in schools)
is_duke_present: bool =  "Duke" in schools

points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100

#print(points)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")
