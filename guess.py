""" Random number guessing game
Author: Andras Marton
Date: 4th January 2020"""

import random
from os import system
import textwrap

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
	_ = system('clear')

def actual_number_message():
	print(color.BOLD + "\nOops.. the actual number was " + color.CYAN + str(num) + color.WHITE + "..." + color.END)

clear()

#  Set the number of attempts the user has to guess
n = 4
i = 1
hello_message = """Howdy! Welcome to the game of Guess The Number. You guessed it right...
The aim of the game is to guess the magic number. You have three chances
to do so. Good luck!
"""

for line in (textwrap.wrap(hello_message, width = 70)):
	print(color.BOLD + line + color.END)

num = random.randint(0,9)
terminate = ("q","quit","exit")

while i < n:
	try:
		guess = input(color.BOLD + "\nEnter your guess: " + color.END)
		if guess in terminate:
			print("\nSee ya another time!")
			break

		else:
			guess = int(guess)
			if num == guess:
				print(color.GREEN + "Well done, your guess was right." + color.END)
				print("\nHowever you win nothing. Thank you for playing.")
				break
			else:
				print(color.RED + "Oh no you guessed it wrong." + color.END)
			#print(color.CYAN + "The number is: " + str(num) + color.END)
			#print(color.CYAN + "Your guess was: " + str(guess) + color.END)
	except ValueError:
		try:
			float(guess)
			print(color.YELLOW + "Please only use integers!" + color.END)
			continue
		except ValueError:
			print(color.YELLOW + "This is not a number! Get it together!" + color.END)
	i = i + 1
else:
	print(color.BOLD + "\nOops.. the actual number was " + color.CYAN + str(num) + color.WHITE + "..." + color.END)
