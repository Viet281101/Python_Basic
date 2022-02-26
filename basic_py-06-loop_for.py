
############################ Exercices of the loop 'For' in Python ###############################



#### Exercices 1: Find the number divisible by 3 from 10 to 50 use 'for'
def exercice_1_first_solution():
	for i in range(1, 50, 1):
		# print(i)
		if i % 3 == 0:
			print(i, end = "  ")


def exercice_1_second_solution():
	for i in range(1, 50, 1):
		# print(i)
		if i % 3 != 0:
			continue
		print(i, end = "  ")




#### Exercices 2: Calcule the sum of factorials: s = 1! + 2! + 3! + ... + 10! use 'for'
def exercice_2(a):
	s = 0
	n = 1
	for i in range(1, a, 1):
		n = i * n
		s = s + n

	return s



#### Exercices 3: Perfect number: find all perfect numbers in the range 1-1000
def exercice_3():
	number = int(input("Enter a number: "))
	s = 0
	for i in range(1, number, 1):
		if number % i == 0:
			s = s + i
	if s == number:
		print(f"Number {number} is the number perfect")
	else:
		print(f"Number {number} is not the number perfect")




def main():

	# Ex1:
	exercice_1_first_solution()

	print()
	print("___" * 20)
	print()

	exercice_1_second_solution()

	print()
	print("___" * 20)
	print()


	# Ex2:
	print("The sum of factorials :", exercice_2(11))

	print()
	print("___" * 20)
	print()


	# Ex3:
	exercice_3()

	print()
	print("___" * 20)
	print()



if __name__ == '__main__':
	main()


