
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



def main():

	# Strings()

	# slicing_strings()

	modify_strings()




if __name__ == '__main__':
	main()

