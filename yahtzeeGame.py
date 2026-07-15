"""
Scoring - top sheet
1 - 6 - 3 rolls
Subtotal for top
63 or higher gets a 35 point bonus
3 of a kind
4 of a kind
Full house - 25
Small Straight - 30 (4 numbers)
Large Straign - 40 (5 numbers)
Chance
Yahtzee
Bonus - 100 point bonus chip but score is recorded in an open spot.
1. Claim the 100 PointsMark a checkmark in the Yahtzee Bonus box on your scorecard.
Each check is worth 100 points at the end of the game.
2. Fill an Open Category (Joker Rules)You must still use the dice roll to fill one of the remaining 12 empty boxes on your scorecard using the following priority:
Upper Section Priority: If the corresponding number box is open, you must score it there. For example, if you roll five 4s, and your "Fours" box is open, you must place it there (scoring 20 points).
Lower Section Joker: If the corresponding Upper Section box is already filled, you can use the roll as a "Joker" in the Lower Section. 
You can score full points in Full House (25 pts), Small Straight (30 pts), or Large Straight (40 pts), even though the dice do not technically match those shapes. 
You can also use it for 3 of a Kind, 4 of a Kind, or Chance.
The Zero Penalty: If the corresponding Upper box is filled and all Lower Section boxes are full, you must place a 0 in one of your remaining open Upper Section boxes (like Ones or Twos).
"""

# Define scoresheet
# Define players
# Create the scoresheet as a class
from random import randint
# create a dice rolling simulation

class Die:
    """A class representing a single die."""
    
    def __init__(self, sides=6):
        """Initialize the die with a given number of sides (default is 6)."""
        self.sides = sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.sides)

class Scoresheet:
    # a class representing a scoresheet
    # creeat the init, it should have teh name of the player
    def __init__(self, playername):
        self.playername = playername

        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixes = 0
        self.upperbonus = 0
        self.threeofakind = 0
        self.fourofakind = 0
        self.fullhouse = 0
        self.smallstraight = 0
        self.largestraight = 0
        self.chance = 0
        self.yahtzee = 0
        self.yahtzeebonuses = 0


class DiceCup:
    # a class to represent the dice roll
    def __init__(self, numberofdice=5):
        self.numberofdice = numberofdice
        self.diceArray = [Die(),Die(),Die(),Die(),Die()]

    def firstroll(self):
        croll = []
        for die in self.diceArray:
            croll.append(die.roll())
            
        return croll
    
    def secondroll(self, dicearray1):
        #dice array 1 is an array of already rolled dice
        indie = 1
        print("Here are the dice you rolled")
        for die in dicearray1:
            print(f"{indie} - {die}")
            indie += 1
        print("Which ones do you want to keep?")
            




die1 = Die()
die2 = Die()
selectionList = ["ones","twos","threes","fours","fives","sixes","threeofakind","fourofakind","fullhouse","smallstraight","largestraight","chance","yahtzee"]

mysheet = Scoresheet("Steve")
print(mysheet.playername)
print(mysheet.ones)
cup = DiceCup()
x = cup.numberofdice
y = cup.diceArray[0].roll()
j = cup.firstroll()
cup.secondroll(j)

