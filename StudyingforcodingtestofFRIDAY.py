#Create a work folder to organize your files and subfolders for this course using Finder


# - Create a “hello world” python program using a text editor 

print("Hello World")
print("Hi my name is Michael Daiello")
#Save a program to a specific location on your file system (i.e., work folder)
#Use Unix commands to navigate your computer file system to specific location
#Use Unix commands to list the contents of a folder and determine your location
#Execute a Python program from the terminal
#Execute a Python program using Python v2 or v3
#Enter the Python interpreter to try out commands and exit correctly


#Correctly create string, int and float variables with descriptive (self commenting) names

#Create a list variable with multiple data items

#Print the values of individual items from the list using the correct index number
#Append, insert, remove, sort and reverse items from/in a list
#Determine the number of items in a list
#Write a program to ask for user input, store the data in a variable
#Create a variable to store the results of a type cast operation (e.g., string to integer)
#Use a chained conditional to test a value against two known values
#Correctly use a for loop to do some operation a specific number of times
#Correctly use a for loop and if statement to do a sequential search through a list
#Correctly use the break statement to exit from a loop
#Correctly use a while loop to make a simple number guessing game

s1 = list();
for i in range(0,9):
   s1[i] = i

print(s1)

#A for loop = A for loop is a counted loop
#with a specific known number of repeats
#This is a loop 
for i in range(5):
	print(i)



myList = [1, 2, 9, 3]
#u can also use strings
myList = ['hi', 'hello', 'etc']

myList.append('why') . .  | . these dd 'why'/9 to the end of myList
myList.append(9) .                        |

myList.upper()  | turns it all to uppercase letters

myList.insert(3, 'hi')
                3 is after how many parts of the list do you want to insert it(like where in the list)

myList.remove('hi')

myList.sort() . orders it(alphabetical/lower to higher)

myList.reverse() reverses the order


myList.reverse() returns how many items in a list







#Below is another piece of code, is using "while"

#guessing game

import random
secret_num = random.randint(0,1000)

num = input("enter a number:")
num = int(num)
chances = 0


while (num!= secret_num):
	if (num > secret_num):
		print("to high")
	elif (num < secret_num):
		print("too low")
	num = int(input("enter a number:"))
	chances = chances + 1 

print("you win! " + "only " + str(chances) + " tries")









