import sys
import random


random_num = random.randint(int(sys.argv[1]), int(sys.argv[2]))
print(f'Guess a number between {int(sys.argv[1])} and {int(sys.argv[2])}: ')

while True:
	try:
		guess = int(input())		
		if int(sys.argv[1]) <= guess <= int(sys.argv[2]):
			if guess == random_num:
				print('That\'s Right!')
				break
			else:
				print('Guess Again!')
		else:
			print(f'Please enter a number between {int(sys.argv[1])} and {int(sys.argv[2])}')
	except ValueError:
		print(f'Please enter a number between {int(sys.argv[1])} and {int(sys.argv[2])}')
		continue

