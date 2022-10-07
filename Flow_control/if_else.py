"""
Moses wants to drive a car and he hears that in planet
zortan there is no age limit for getting a lecense.
"""

age: int = 13
planet: str = "Earth"
planet: str = "Zortan"

# -------------------------
#  And / Statement
# --------------------------

if age < 16 and planet == "Earth":
    # Evaluation - True and True => True
    print("You are Not eligible for a license on earth")
    # Evaluation stops here and we exit If/Else block
    # ^---------------------------------------------^
elif age > 16 and planet == "Earth":
    # Execution does not reach here
    # Evaluation - False and True => False
    print("You can apply for a license on Earth")
elif age < 16 and planet == "Zortan":
    # Execution does not reach here
    # Evaluation - True or False => True
    print("You can apply for a Zortanian license!")
