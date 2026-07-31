import sys
import termios
import tty

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
    return ch

print("Press any key...")

char = "1"
while char != "q":
    char = getch()
    print(f"You pressed: {char}")
