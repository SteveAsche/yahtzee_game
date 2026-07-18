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

        self.ones = -1
        self.twos = -1
        self.threes = -1
        self.fours = -1
        self.fives = -1
        self.sixes = -1
        self.upperbonus = -1
        self.threeofakind = -1
        self.fourofakind = -1
        self.fullhouse = -1
        self.smallstraight = -1
        self.largestraight = -1
        self.chance = -1
        self.yahtzee = -1
        self.yahtzeebonuses = -1

    def printsheet(self):
        global selectionList
        for item in selectionList:
            print(f"{item.title()} = {getattr(self, item)}")


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
        print("Which ones do you want to keep? ")
        selection = input("Enter the numbers of the ones you want to keep: ")
        # print(selection)
        # print(type(selection))
        #parse the selection
        strlist = selection.split(",")
        # print(strlist)
        int_list = [int (x) for x in strlist] #convert to integers
        # print(int_list)
        for x in range(5):
            if (x+1) in int_list:
                continue
            else:
                dicearray1[x] = randint(1,6)
        # print(dicearray1)
        #
        indie = 1
        print("Here are the results of your second roll ")
        for die in dicearray1:
            print(f"{indie} - {die}")
            indie += 1
        print("Which ones do you want to keep? ")
        selection = input("Enter the numbers of the ones you want to keep: ")
        # print(selection)
        # print(type(selection))
        #parse the selection
        
        strlist = selection.split(",")
        # print(strlist)
        int_list = [int (m) for m in strlist] #convert to integers
        # print(int_list)
        x=0
        for x in range(5):
            if (x+1) in int_list:
                continue
            else:
                dicearray1[x] = randint(1,6)
        print("Here is your final result")
        for die in dicearray1:
            print(f"{indie} - {die}")
            indie += 1
        #print(dicearray1)
        return dicearray1

            

def wheretoscore(fivedice, playersheet):
    global selectionList
    print("you have the following dice")

    for die in fivedice:
        print(f"- {die}")
    print("How do you want to score them")
    playersheet.printsheet()

    invalid = True
    while invalid:
        scoreHere = input("Type the category where you want to score: ")
        scoreHere = scoreHere.strip().lower()
        if scoreHere in selectionList:
            # valid choice 
            if getattr(playersheet, scoreHere) == -1:
                # okay to score it here
                # test the dice against the category  - this should be a function
                match scoreHere:
                    case "ones":
                        newval = fivedice.count(1) * 1
                        #setattr(playersheet, scoreHere, newval)
                    case "twos":
                        newval = fivedice.count(2) * 2
                        #setattr(playersheet, scoreHere, newval)
                    case "threes":
                        newval = fivedice.count(3) * 3
                        #setattr(playersheet, scoreHere, newval)
                    case "fours":
                        newval = fivedice.count(4) * 4
                        #setattr(playersheet, scoreHere, newval)
                    case "fives":
                        newval = fivedice.count(5) * 5
                        #setattr(playersheet, scoreHere, newval)
                    case "sixes":
                        newval = fivedice.count(6) * 6
                        #setattr(playersheet, scoreHere, newval)
                    case "threeofakind":
                        if any(fivedice.count(x) >= 3 for x in set(fivedice)):
                            newval = sum(fivedice)
                            #setattr(playersheet, scoreHere, newval)
                        else:
                            print("You don't have three of a kind.  You'll take a zero (0) in this category")
                            newval = 0
                            #setattr(playersheet, scoreHere, newval)
                    case "fourofakind":
                        if any(fivedice.count(x) >= 4 for x in set(fivedice)):
                            newval = sum(fivedice)
                            #setattr(playersheet, scoreHere, newval)
                        else:
                            print("You don't have four of a kind.  You'll take a zero (0) in this category")
                            newval = 0
                            #setattr(playersheet, scoreHere, newval)
                    case "fullhouse":
                        counts = [fivedice.count(x) for x in set(fivedice)]
                        if 3 in counts and 2 in counts:
                            newval = 25
                        else:
                            print("you don't have a full house")
                            newval = 0
                    case "smallstraight":
                        # Convert to a sorted list of unique numbers to remove duplicates (like)
                        unique_dice = sorted(list(set(fivedice)))
                        unique_string = "".join(str(x) for x in unique_dice)
        
                        # Check if any of the three possible small straight sequences are hidden inside the string
                        if "1234" in unique_string or "2345" in unique_string or "3456" in unique_string:
                            newval = 30
                        else:
                            newval = 0
                            print("You don't have a small straight.  You'll get zero in this category")
                    case "largestraight":
                        sorted_dice = sorted(fivedice)
                        # There are only two possible combinations for a large straight
                        if sorted_dice == [1, 2, 3, 4, 5] or sorted_dice == [2, 3, 4, 5, 6]:
                             newval = 40
                        else:
                            newval = 0
                            print("You don't have a large straight.  You get a 0")

    
                setattr(playersheet, scoreHere, newval)


                invalid = False
            else:
                print("Not that section has been scored before")
        else:
            print("invalid category")
                    

def printSheet(playersheet):
    global selectionList
    for item in selectionList:
        print(f"{item.title()} = {getattr(playersheet, item)}")


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
k = cup.secondroll(j)
# k is an array so we will sort it
k.sort()

print(k)

wheretoscore(k, mysheet)
mysheet.printsheet()

