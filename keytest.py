import sys
import termios
import tty

darray1 = [1,6,4,3,1]
def getch():
    # Save the current terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # Set the terminal to raw mode to catch raw keystrokes
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        # Always restore the terminal settings afterward
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch.lower()

def modifylist(dicearrayz):
    print(dicearrayz)
    pulllist = dicearrayz.copy()
    cleanup = False
    cuplist = []
    returnlist = []
    validentries = ["1","2","3","4","5","6","n","a","q"]
    print("Which numbers do you want to roll again. Enter the number to add to the cup. Enter 'q' to end or 'a' for all or 'n' for none")
    char = 'z'
    while char != 'q':
        char = getch()
        if char in validentries:
            print(f"you pressed {char}")
#            continue
            if char == "a":
                print("You selected all dice to be rolled again")
                if cleanup:
                    print("are you sure you want to do this 'y' ")
                    chud = getch()
                    if chud == "y":
                        returnlist = []
                        print("confirmed")
                        break
                    else:
                        print(f"new pullist {pulllist}")
                        print(f"cuplist {cuplist}")
                else:
                    returnlist = []
                    break
            elif char == "n":
                print("You selected no dice to be put into the cup")
                if cleanup:
                    print("Are you sure you want to do this hit 'y' if yes, anything else if no")
                    chud = getch()
                    if chud == "y":
                        returnlist = [1,2,3,4,5]
                        print("confirmed")
                        break
                    else:
                        print(f"new pullist {pulllist}")
                        print(f"cuplist {cuplist}")
                else:
                    returnlist = [1,2,3,4,5]
                    break
                        
            elif char == "q":
                break
            else:
                #find the index of the number picked
                tvalue = int(char)
                if tvalue in pulllist:
                    print("Valid entry")
                    idx = pulllist.index(tvalue)
                    #print(f"{tvalue} is at index {idx} in pulllist")
                    #print(pulllist)
                    pulllist.remove(tvalue)
                    cuplist.append(tvalue)
                    cleanup = True
                    print(f"new pullist {pulllist}")
                    print(f"cuplist {cuplist}")
                    # put it in the cup update the pullist update the returnlist
                    if len(pulllist) == 0:
                        print("remember to hit 'q' to finish")
                else:
                    print("that number is not in the roll")

        else:
            print("not a valid entry")
    # at this point we've left the while loop cleanup the cuplist by comparing it against the dicearray
    # the values will not be in the cuplist if they were not in the original array.  So we can ignore inaccurate values
    if cleanup:
        #print("called")
        newdex = 0
        usedIndexes = []
        returnlist = []
        #print(dicearray)
        for n in cuplist:
            #print(f"n = {n}")
            idi = 1
            for d in dicearrayz:
                #print(f"n= {n} d= {d}")
                if n == d and (idi not in usedIndexes):
                    returnlist.append(idi)
                    usedIndexes.append(idi)
                    break
                idi += 1



    return returnlist
        





print("Press any key...")
print(modifylist(darray1))


char = "1"
while char != "q":
    char = getch()
    print(f"You pressed: {char}")
