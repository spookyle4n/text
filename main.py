import time
from colorama import init, Fore, Style

# Initialize colorama
init()

# Set the text to be displayed
text = "·▄▄▄▄        ▐▄• ▄  ▄ .▄      ▄• ▄▌ ▐ ▄ ·▄▄▄▄  \n" \
       "██▪ ██ ▪      █▌█▌▪██▪▐█▪     █▪██▌•█▌▐███▪ ██ \n" \
       "▐█· ▐█▌ ▄█▀▄  ·██· ██▀▐█ ▄█▀▄ █▌▐█▌▐█▐▐▌▐█· ▐█▌\n" \
       "██. ██ ▐█▌.▐▌▪▐█·█▌██▌▐▀▐█▌.▐▌▐█▄█▌██▐█▌██. ██ \n" \
       "▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀▀▀▀ · ▀█▄▀▪ ▀▀▀ ▀▀ █▪▀▀▀▀▀• "

# Set the initial text color to red
color = Fore.RED

# Set the interval at which the text color should change (in seconds)
interval = 0.1

while True:
    # Set the text color
    print(color + text)
    # Reset the text color back to default
    print(Style.RESET_ALL)

    # Change the text color to the next color in the rainbow
    if color == Fore.RED:
        color = Fore.YELLOW
    elif color == Fore.YELLOW:
        color = Fore.GREEN
    elif color == Fore.GREEN:
        color = Fore.BLUE
    elif color == Fore.BLUE:
        color = Fore.MAGENTA
    elif color == Fore.MAGENTA:
        color = Fore.RED

    # Sleep for the specified interval before changing the text color again
    time.sleep(interval)
