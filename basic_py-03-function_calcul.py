
######################### Function round(), eval(), random() in Python ###############################


# import library 
import random
# or like this to use directly randrange from random:
# from random import randrange



# A small number guessing game to pratice random()
def guessing_nbr_game():
	the_nbr = random.randint(1, 10)
	guess = int(input("Guess a number between 1 and 10: "))

	while guess != the_nbr:
		if guess > the_nbr:
			print(guess, "was too high. Try again.")
		if guess < the_nbr:
			print(guess, "was too low. Try again. ")
		guess = int(input("Guess again: "))
	print(guess, "was the number !! You win !")



def main():

	### Rounding number : round()
	a = float(input("Enter a decimal, (for example: 3.141592654): "))
	print("Round: ", round(a))
	print("Round to units 2: ", round(a, 2))
	print("Round to units 3: ", round(a, 3))
	
	print()
	print("-" * 20)
	print()

	### automatically calculate a string number:  eval()
	s = "2 + 5 * 8 / 9 ** 5"
	print(type(s))
	print(eval(s))


	print()
	print("-" * 20)
	print()


	### function to get a random number from a list: random()
	random_nbr = random.randrange(1, 100)

	print("A random number from 1 to 100", random_nbr)



	


if __name__ == '__main__':
	main()

