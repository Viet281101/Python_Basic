
##################################### The loop of 'for' exercices ####################################


def multiplication_table():
	for i in range(2, 10, 1):
		# print(i)
		for j in range(2, 10, 1):
			print(i, " * ", j, " = ", i*j)
		print("-" * 20)


def print_letter_N(n):
	for i in range(n):
		for j in range(n):
			if j == 0 or j == (n - 1) or i == j:
				print("*", end = " ")
			else:
				print(" ", end = " ")
		print()


def print_letter_N_reverse(n):
	for i in range(n):
		for j in range(n):
			if j == 0 or j == (n - 1) or i+j == (n-1):
				print("*", end = " ")
			else:
				print(" ", end = " ")
		print()


def print_heart():
	for i in range(7):
		for j in range(7):
			if (i==0 and j in (1,2,4,5)) or (i==1 and j in (0,3,6)) or (i==2 and j in (0,6)) or (i==3 and j in (1,5)) or (i==4 and j in (2,4)) or (i==5 and j==3):

				print("*", end = "   ")

			else:
				print("", end = "   ")
		print()




def main():
	n = int(input("Enter the size this 'N' character: "))

	###### print multiplication table using loop:

	# multiplication_table()


	###### print * in the shape of a letter N:
	print_letter_N(n)
	print()


	print("-" * 40)
	print()


	###### print * in the shape of a letter N but reverse:
	print_letter_N_reverse(n)
	print()


	print("-" * 40)
	print()


	###### print * in the shape of heart:
	print_heart()



if __name__ == '__main__':
	main()

