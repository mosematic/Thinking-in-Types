"""
Moses wants to drive a car and he hears that in planet
zortan there is no age limit for getting a lecense.
"""

age: int = 13
planet: str = "Earth"

# -------------------------
#  And / Statement
# --------------------------

if age < 16 and planet == "Earth":
    print("You are Not eligible for a license on earth")
elif age > 16 and planet == "Earth":
    print("You can apply for a license on Earth")
elif age < 16 and planet == "Zortan":
    print("You can apply for a Zortanian license!")
