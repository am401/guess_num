""" Random number guessing game
Author: Andras Marton
Date: 4th January 2020"""

import random

class color:
	BOLD = '\033[1m'
	CYAN = '\033[96m'
	RED = '\033[91m'
	GREEN = '\033[92m'
	END = '\033[0m'

while True:
	try:
		num = random.randint(0,10)
		guess = input(color.BOLD + "\nEnter your guess: " + color.END)
		if guess == 'q':
				break
		else:
			guess = int(guess)
			if num == guess:
				print(color.GREEN + "Well done, your guess was right." + color.END)
			else:
				print(color.RED + "Oh no you guessed it wrong." + color.END)
			print(color.CYAN + "The number is: " + str(num) + color.END)
			print(color.CYAN + "Your guess was: " + str(guess) + color.END)
	except ValueError:
		try:
			float(guess)
			print("Please only use integers!")
			continue
		except ValueError:
			print("This is not a number! Get it together!")