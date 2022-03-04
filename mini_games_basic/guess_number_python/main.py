
import random



def guess_nbr_user(x):
	random_nbr = random.randint(1, x)
	guess = 0

	while guess != random_nbr:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess < random_nbr:
			print('Sorry, guess again. Too low.')
		elif guess > random_nbr:
			print('Sorry, guess again. Too high.')

	print(f'Congratulation ! The number {random_nbr} is the correct number !')



def guess_nbr_computer(x):
	low = 1
	high = x
	feedback = ''

	while feedback != 'c':
		guess = random.randint(low, high)


def main():
	guess_nbr_user(10)



if __name__ == '__main__':
	main()

