"""
Friends from Earth want to know were is Moses, so Moses decides to 
write a program that will make his friends guess the name of planet.
"""

correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

# --------------------------
# Alternative 1
# ---------------------------

while correct_guess is not True:
    guess = input("Moses Says: Can you guess my planet? >>> ")
    if guess.lower() == planet.lower():
        print("Right guess!! Moses is at Zortan")
        correct_guess = True
    else:
        print("Moses says: Wrong choice, try again!")
