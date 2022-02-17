
##################### Exercises to calculate recursive functions in python ########################



def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)



# Enter the value n to calcule fibonacci F(n):
# Example: F1 = 1, F2 =2, F(n) = F(n - 1) + F(n - 2)
def fibonacci(n):
	if (n == 1 or n == 2):
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)




def main():

	# Factorial:
	a = factorial(8)
	print("Factorial of 8 = ",a)
	##  = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1


	print()
	print("-" * 20)
	print()


	# Fibonacci
	print("With F1 = 1, F2 =2, F(n) = F(n - 1) + F(n - 2)")
	# print("F(12) = ",fibonacci(12))
	# print("F(3) = ",fibonacci(3))
	# print("F(4) = ",fibonacci(4))

	n = int(input("Enter n: "))
	for i in range(1, n + 1, 1):
		print("F(", i, ") = " , fibonacci(i))




if __name__ == '__main__':
	main()

