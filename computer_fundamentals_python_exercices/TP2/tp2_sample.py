#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:28:51 2021

@author: revekka
"""

#import csv
import csv



#initialise the following sets:
    
l3_students = set()
#info_students = ##########
#math_students = #########
#excellent_students = ########

#-----------------------------------------------------------------------------
#read the all_students.csv file 
with open("l3_students.csv",newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["First name"],row["Last name"])
        #add each row to the set l3_students
        l3_students.add(row["First name"]+" "+row["Last name"])
            
print(l3_students) 

#-----------------------------------------------------------------------------
#read the info_students.csv file and add each row to the info_students set


#-----------------------------------------------------------------------------
#read the math_students.csv file and add each row to the math_students set

#-----------------------------------------------------------------------------
#read the excellent_students.csv file and add each row to the excellent_students set


#-----------------------------------------------------------------------------

