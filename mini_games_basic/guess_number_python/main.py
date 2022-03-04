
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

	while feedback != 'c' and low != high:
		if low != high:
			guess = random.randint(low, high)
		else:
			# could also be high b/c low = high
			guess = low
		feedback = input(f'Is {guess} too high (H), too low (L), or correct (C) ? ').lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1

	print(f'The computer guessed your number, that is {guess} !!')


def main():

	# guess_nbr_user(10)

	guess_nbr_computer(10)



if __name__ == '__main__':
	main()

