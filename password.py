#
#passord.py - let's a user try to match password 3 times
#mdaiello - original coding, October 30th, 2018
#

secret = "joe"

for i in range(3):
	pword = input("enter a password: ")

	if (secret == pword):
		print("welcome")
		break
	else:
		print("incorrect . . .")
