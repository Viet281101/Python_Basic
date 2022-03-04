
######################################### List in Python ########################################





#### Example list: 

def type_list():
	n = int(input("Enter number of element in list: "))
	lst = [0] * n
	print(lst)
	print(type(lst))


def string_element():
	lst = ['y', "k", """ffffffffffffff""", '''ajshfkafjasjkdalksdjakl''']
	print(lst)


## Join Two Lists
def join_lists():
	lst = [0, 1, 2, 3, 4]
	lst_2 = ["python", "excel"]
	lst_3 = [lst, lst_2]
	print(lst_3)


## Append list2 into list1:
def join_to_list1():
	list1 = ["a", "b" , "c"]
	list2 = [1, 2, 3]
	for x in list2:
		list1.append(x)
	print(list1) 


## Use the extend() method to add list2 at the end of list1:
def join_with_extend():
	list1 = ["a", "b" , "c"]
	list2 = [1, 2, 3]

	list1.extend(list2)
	print(list1) 


def length_list():
	thislist = ["apple", "banana", "cherry"]
	print(len(thislist))




#### Access List Items:

## print a item in list with index number
def second_item():
	thislist = ["apple", "banana", "cherry"]
	print(thislist[1])


def negatif_index():
	thislist = ["apple", "banana", "cherry"]
	print(thislist[-1])


def range_index_1():
	thislist = ["apple", "banana", "cherry"]
	print(thislist[-1])


def range_index_2():
	thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(thislist[:4])


def range_index_3():
	thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(thislist[2:])


def range_negatif_index():
	thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
	print(thislist[-4:-1])


def check_item_exists():
	thislist = ["apple", "banana", "cherry"]
	if "apple" in thislist:
		print("Yes, 'apple' is in the fruits list") 





#### Change List Items:

def change_item_value():
	thislist = ["apple", "banana", "cherry"]
	thislist[1] = "blackcurrant"
	print(thislist)


def change_range_item_value():
	thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
	thislist[1:3] = ["blackcurrant", "watermelon"]
	print(thislist)


## Change the second value by replacing it with two new values: 
def change_range_item_value_2():
	thislist = ["apple", "banana", "cherry"]
	thislist[1:2] = ["blackcurrant", "watermelon"]
	print(thislist) 

### ==> The length of the list will change when the number of items inserted does not match the number of items replaced.


## Change the second and third value by replacing it with one value:
def change_range_item_value_3():
	thislist = ["apple", "banana", "cherry"]
	thislist[1:3] = ["watermelon"]
	print(thislist) 


## Insert a element into list:
def insert_items():
	thislist = ["apple", "banana", "cherry"]
	thislist.insert(2, "watermelon")
	print(thislist)






#### Add List Items

## To add an item to the end of the list, use the append() method:
def append_items():
	thislist = ["apple", "banana", "cherry"]
	thislist.append("orange")
	print(thislist)


## To append elements from another list to the current list, use the extend() method:
def extend_list():
	thislist = ["apple", "banana", "cherry"]
	tropical = ["mango", "pineapple", "papaya"]
	thislist.extend(tropical)
	print(thislist)


## The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
def add_any_iterable():
	thislist = ["apple", "banana", "cherry"]
	thistuple = ("kiwi", "orange")
	thislist.extend(thistuple)
	print(thislist)






#### Remove List Items

## The remove() method removes the specified item.
def remove_items():
	thislist = ["apple", "banana", "cherry"]
	thislist.remove("banana")
	print(thislist)


## The pop() method removes the specified index.
def pop_list():
	thislist = ["apple", "banana", "cherry"]
	thislist.pop(1)
	print(thislist)


## If you do not specify the index, the pop() method removes the last item.
def remove_last_item():
	thislist = ["apple", "banana", "cherry"]
	thislist.pop()
	print(thislist)


## The del keyword also removes the specified index:
def remove_first_item():
	thislist = ["apple", "banana", "cherry"]
	del thislist[0]
	print(thislist)


## The del keyword can also delete the list completely.
def delete_entire_list():
	thislist = ["apple", "banana", "cherry"]
	del thislist 


## The clear() method empties the list. The list still remains, but it has no content.
def clear_list():
	thislist = ["apple", "banana", "cherry"]
	thislist.clear()
	print(thislist)





#### Loop Lists

## We can loop through the list items by using a for loop:
def print_list_by_loop():
	thislist = ["apple", "banana", "cherry"]
	for x in thislist:
		print(x)


## We can also loop through the list items by referring to their index number. Use the range() and len() functions to create a suitable iterable.
def print_list_by_loop_index():
	thislist = ["apple", "banana", "cherry"]
	for i in range(len(thislist)):
		print(thislist[i])


## Print all items, using a while loop to go through all the index numbers
def print_item_while_loop():
	thislist = ["apple", "banana", "cherry"]
	i = 0
	while i < len(thislist):
		print(thislist[i])
		i = i + 1


## A short hand for loop that will print all items in a list:
def print_item_short_for():
	thislist = ["apple", "banana", "cherry"]
	[print(x) for x in thislist]






#### List Comprehension

### The syntax: newlist = [expression for item in iterable if condition == True]

def list_comprehension():
	fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
	newlist = []
	for x in fruits:
		if "a" in x:
			newlist.append(x)
	print(newlist) 


## With list comprehension in one line of code:
def list_comprehension_short():
	fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
	# only print the element with character 'a' inside it
	newlist = [x for x in fruits if "a" in x]
	print(newlist)






#### Sort Lists

## List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
def sort_list_alphanumerically():
	# Sort the list alphabetically:
	thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
	thislist.sort()
	print(thislist)

	# Sort the list numerically:
	thislist = [100, 50, 65, 82, 23]
	thislist.sort()
	print(thislist)


## To sort descending, use the keyword argument reverse = True:
def sort_descending():
	# Sort the list descending:
	thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
	thislist.sort(reverse = True)
	print(thislist)

	# Sort the ist descending:
	thislist = [100, 50, 65, 82, 23]
	thislist.sort(reverse = True)
	print(thislist)





#### Reverse Order

## The reverse() method reverses the current sorting order of the elements.
def reverse_order():
	thislist = ["banana", "Orange", "Kiwi", "cherry"]
	thislist.reverse()
	print(thislist)





#### Copy Lists

## There are ways to make a copy, one way is to use the built-in List method copy().

# Make a copy of a list with the copy() method:
def copy_list_copy():
	thislist = ["apple", "banana", "cherry"]
	mylist = thislist.copy()
	print(mylist)


# Make a copy of a list with the list() method:
def copy_list_list():
	thislist = ["apple", "banana", "cherry"]
	mylist = list(thislist)
	print(mylist)





def main():

	###### Test any function up there to see how it works :

	# type_list()

	# string_element()

	# join_lists()

	length_list()






if __name__ == '__main__':
	main()
