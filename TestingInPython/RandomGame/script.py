import sys
import random

def run_guess(guess, answer):
	if 0 < guess < 11:
		if guess == answer:
			print('That\'s Right!')
			return True
	else:
		print('Please enter a number between 1 and 10!')
		return False

if __name__ == '__main__':
	answer = random.randint(1, 10)
	while True:
		try:
			guess = int(input('Guess a number between 1 and 10: '))		
			if (run_guess(guess, answer)):
				break
		except ValueError:
			print('Please enter a number')
			continue