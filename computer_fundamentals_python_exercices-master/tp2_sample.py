#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:28:51 2021

@author: revekka
"""

#3/ Importer la bibliothèque csv "import csv":
import csv
import os


os.system('clear')

#4/ initialiser un ensemble pour chaque catégorie d’élèves:
    
l3_students = set()
all_students = set()
excellent_students = set()
info_students = set()
math_students = set()

#info_students = ##########
#math_students = #########
#excellent_students = ########


# 5/ 6/

#-----------------------------------------------------------------------------
#all_students.csv fichier:
with open("l3_students.csv",newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["First name"],row["Last name"])
        #add each row to the set l3_students
        l3_students.add(row["First name"]+" "+row["Last name"])
            
print('\n----------------------------------------\n')
print("Il y a {} élèves dans l3_students ".format(len(l3_students)))
print('\n----------------------------------------\n')


#-----------------------------------------------------------------------------
#info_students.csv fichier:

with open("info_students.csv",newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["First name"],row["Last name"])
        #add each row to the set l3_students
        info_students.add(row["First name"]+" "+row["Last name"])

# chaque ligne sur info_students 
print('\n----------------------------------------\n')
print("Il y a {} élèves dans info_students ".format(len(info_students)))
print('\n----------------------------------------\n')


#-----------------------------------------------------------------------------
#math_students.csv fichier:

with open("math_students.csv",newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["First name"],row["Last name"])
        #add each row to the set l3_students
        math_students.add(row["First name"]+" "+row["Last name"])

# chaque ligne sur math_students
print('\n----------------------------------------\n')
print("Il y a {} élèves dans math_students ".format(len(math_students)))
print('\n----------------------------------------\n')



#-----------------------------------------------------------------------------
#excellent_students.csv fichier:

with open("excellent_students.csv",newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["First name"],row["Last name"])
        #add each row to the set l3_students
        excellent_students.add(row["First name"]+" "+row["Last name"])

# chaque ligne sur excellent_students
print('\n----------------------------------------\n')
print("Il y a {} élèves dans excellent_students ".format(len(excellent_students)))
print('\n----------------------------------------\n')

#-----------------------------------------------------------------------------


#7/ Excellent_students sont qui intéressent l’entreprise


#8/

students_final = set()

for E in math_students and info_students:
    if E in math_students or info_students and excellent_students :
        students_final.add(E)

print("Final_students :\n")
for e in students_final :
    print(e)

print('\n----------------------------------------\n')



#9/

print('le sous-ensemble des élèves en informatique et étant dans students_final est :\n')
for i in students_final and info_students :
    print(i)

print('\n----------------------------------------\n')



#10/

print('le sous-ensemble des élèves en math et étant dans students_final est :\n')
for j in students_final and math_students :
    print(j)

print('\n----------------------------------------\n')