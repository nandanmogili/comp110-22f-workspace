"""Some tender, loving functions? """

def love(subject:str)-> str:
    """Given a subject as a paramter, returns a loving string"""
    return f"I love you {subject}!" # instead of using + and concatenation, u you use a f string



def spread_love(to:str, n:int)-> str:
    """Generates a str repeating a loving message n times"""
    love_note: str = ""
    i:int = 0
    while i<n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

#print(spread_love("Nandan", 6))
