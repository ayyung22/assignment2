# -------------------------------------------------------- #
# Assignment 2: Python Loops and Object Types
# CIS 103: Introduction to Programming
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/6/2024


#Exercise 1: While Loop
import string

print("Exercise 1: While Loop")
num = 1
while num <= 10:
    if num == 5:
        break
    print (num)
    num += 1

print()
print()

#Exercise 2: For Loop
print("Exercise 2: For Loop")
string.ascii_letters = 'CIS103'
for ch in string.ascii_letters:
    print(ch, ord(ch))

print()
print()

##Exercise 3: Nested Loop
print("Exercise 3: Nested Loop")
for i in range(1,6):
    for j in range(i):
        print('*', end='')
    print()

print()
print()

#Exercise 4: String Operations
print("Exercise 4: String Operations")
def reverse_string(s):
    return s[::-1]

my_string = "Lab2Assignment"
print(reverse_string(my_string))

print()
print()

#Writing a function that formats output for given variables
name = 'John'
age = 30
salary = '$50000.50'

print(f"Name:{name}, Age:{age}, Salary:{salary}")

print()
print()

#Exercise 5: List Operations
list = [6, 7, 8, 9, 10, 11]

#append 12 to the list
list.append(12)

#22 must be inserted at the 3rd index
list.insert(3, 22)

#sorting list in ascending order
list.sort()

#popping the last element of the list
list.pop(7)

#removing 8 from the list
list.pop(2)

print(list)

print()
print()

#Exercise 6: Tuples
my_tuple = (19, 20, 21, 22, 23)

# Print first and last elements
print("Exercise 6: Tuples")
print("First element:", my_tuple[0]) # 19
print("Last element:", my_tuple[-1]) # 23

# Attempt to modify the second element
try:
    my_tuple[1] = 10
except TypeError as e:
    print("Error:", e)

print()
print()

#Exercise 7: Dictionary Operations
print("Exericse 7: Dictionary Operations")
student_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Add salary
student_dict['Salary'] = 50000.50 #Salary = 50000.50

# Modify age
student_dict['age'] = 30 # age = 30

# Remove city
student_dict.pop('city') # no more New York

# Print all keys and values
for key, value in student_dict.items():
    print(f"{key}: {value}")

print()
print()


#Exercise 8: Break and Continue
print ("Exercise 8: Break and Continue")

num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    if num == 8:
        break
    print (num)
