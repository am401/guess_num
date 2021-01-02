import random
import os
import sys


class color:
    BOLD = '\033[1m'
    WHITE = '\033[37m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'
    YELLOW = '\033[33m'


def clear():
    """Clear the screen at the start of the script"""
    _ = os.system('clear')


def header():
    print("+" * 10 + " Main Menu " + "+" * 10 + "\n")
    print("1) Play the game\n2) Score board\n3) Exit\n")


def guess_the_number(guess, num):
    terminate = ("q","quit","sys.exit")
    try:
        if guess in terminate:
            print("\nSee ya another time!")
            sys.exit()
        else:
            guess = int(guess)
            if num == guess:
                print(color.GREEN + "Well done, your guess was right." + color.END)
                print("\nHowever you win nothing. Thank you for playing.")
                sys.exit()
            else:
                print(color.RED + "Oh no your guess is wrong." + color.END)
    except ValueError:
            try:
                float(guess)
                print(color.YELLOW + "Please only use integers!" + color.END)
            except ValueError:
                print(color.YELLOW + "This is not a number! Get it together!" + color.END)


if __name__ == '__main__':
    clear()
    header()
    while True:
        choice = input("Please enter your choice: ")
        if choice == "1":
            n = 4
            i = 1
            num = random.randint(0,9)
            print("Guess the number to win! The number will be between " + color.YELLOW + "0" + color.END + " and " + color.YELLOW + "9" + color.END + "!")
            while i < n:
                guess = input(color.BOLD + "\nEnter your guess: " + color.END)
                guess_the_number(guess, num)
                i = i + 1
            else:
                print(color.BOLD + "\nOops.. the actual number was " + color.CYAN + str(num) + color.WHITE + "...\n" + color.END)

        elif choice == "2":
            print("This is coming soon...")
        elif choice =="3":
            #sys.exit()
            break
        else:
            print("Incorrect input detected: " + choice + " is not a valid response")
            print("Please try again.")
        header()
