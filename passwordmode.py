#
#passord.py - let's a user try to match password 3 times
#mdaiello - original coding, October 30th, 2018
#

secret = "joe"

x=1

while(x<2):
	
	print("try again")
	pword = input("enter a password: ")

	if (secret == pword):
		print("welcome")
		break
	else:
		print("incorrect . . .")



