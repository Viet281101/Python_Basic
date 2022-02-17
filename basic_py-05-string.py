
################################## Strings in python ##################################




def Strings():
	a = "Hello, World!"

	# a = """Lorem ipsum dolor sit amet,
	# consectetur adipiscing elit,
	# sed do eiusmod tempor incididunt
	# ut labore et dolore magna aliqua."""

	print(a) 
	print("a[1] : ", a[1])
	print("The length of string a : ", len(a))



	print()
	print("-" * 20)
	print()

	# Since strings are arrays, we can loop through the characters in a string, with a for loop.
	for x in "banana":
  		print(x)

	print()
	print("-" * 20)
	print()



  	# To check if a certain phrase or character is present in a string, we can use the keyword in.
	txt = "The best things in life are free!"
	print("free" in txt)

	if "free" in txt:
  		print("Yes, 'free' is present.")


  	# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
	print("expensive" not in txt)

	if "expensive" not in txt:
  		print("No, 'expensive' is NOT present.")	



def slicing_strings():
	b = "Hello, World!"

	print("Get the characters from position 2 to position 5 (not included):", b[2:5])
	print("Get the characters from the start to position 5 (not included): ", b[:5])
	print("Get the characters from position 2, and all the way to the end:", b[2:])
	print('From: "o" in "World!" (position -5) to, but not included: "d" in "World!" (position -2):', b[-5:-2])




def modify_strings():
	a = "Hello, World!"
	b = " meow "
	
	# Upper and lower string :
	print("The origin : ", a)
	print("The upper() method returns the string in upper case: ", a.upper())
	print("The lower() method returns the string in lower case:", a.lower())

	print()
	print("-" * 20)
	print()

	# strip 
	print("The origin : ")
	print(b)
	print("The strip() method removes any whitespace from the beginning or the end:")
	print(b.strip())

	print()
	print("-" * 20)
	print()

	# Replace string
	print("The replace() method replaces a string with another string: ", a.replace("H", "J"))

	print()
	print("-" * 20)
	print()

	# Split string
	print("The split() method splits the string into substrings if it finds instances of the separator: ", a.split(","))



def concatenation_strings():
	a = "Hello"
	b = "World"

	c = a + " " + b
	print(c)




def format_strings():
	age = 36

	# txt = "My name is John, I am " + age
	# print(txt)


	# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
	txt = "My name is John, and I am {}"
	print("Use the format() method to insert numbers into strings: ")
	print(txt.format(age))

	print()
	print("-" * 20)
	print()

	# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
	quantity = 3
	itemno = 567
	price = 49.95

	myorder = "I want {} pieces of item {} for {} dollars."
	print(myorder.format(quantity, itemno, price))	


	print()
	print("-" * 20)
	print()

	# can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
	my_order = "I want to pay {2} dollars for {0} pieces of item {1}."
	print(my_order.format(quantity, itemno, price))





def main():

	# Strings()

	# slicing_strings()

	# modify_strings()

	# concatenation_strings()

	format_strings()




if __name__ == '__main__':
	main()

