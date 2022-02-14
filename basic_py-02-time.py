
###############################  The function 'time()' in python exercices: ##########################


# import library 
import time


def calculate_your_age(year_birth):
	time_3 = time.localtime()
	return (time_3.tm_year - year_birth)


def main():
	# Returns the number of seconds, from 0:0:00 on 1/1/1970 in utc time, called epoch(time start time)
	second = time.time()
	print(second)


	# convert seconds from epoch (0h00 1/1/1970) to string
	now = time.ctime(second)
	print(now)


	# Returns current time, year, month, week in local time
	time_3 = time.localtime()
	print(time_3)
	print("This year is : ", time_3.tm_year)
	print("This month is : ", time_3.tm_mon)
	print("Today is : ", time_3.tm_mday)
	print("This hour is : ", time_3.tm_hour)


	# Returns current year month week local time
	time_string = time.strftime("%m /%d/ %y, %H:%M:%S ", time_3)
	print(time_string)

	# class <str>
	# print(type(time_string))


	# small exercices to calcule your age by function 'time()'
	year_birth = int(input("Enter your year of birth: "))
	if year_birth > time_3.tm_year or year_birth <= 0:
		print("That's not your year of birth !!")
	else:
		print("You are ", calculate_your_age(year_birth), "years old !")
		print("The year that you are 100 years old is: ", year_birth + 100)


	# delay program execution in seconds
	print("Start counting time")
	time.sleep(5)
	print("Stop counting !")




if __name__ == '__main__':
	main()

