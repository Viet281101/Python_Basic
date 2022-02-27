
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


def merge_list():
	lst = [0, 1, 2, 3, 4]
	lst_2 = ["python", "excel"]
	lst_3 = [lst, lst_2]
	print(lst_3)


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





def main():

	# type_list()

	# string_element()

	# merge_list()

	length_list()






if __name__ == '__main__':
	main()
