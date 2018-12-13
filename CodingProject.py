import os 
input ("Hello and Welcome to your personal expense manager")
print = ("Would you like to create some finacial goals?")

x1 = input("Expense 1: ")
x1 = int(x1)

y1 = input("Expense 2: ")
y1 = int(y1)

x2 = input("Expense 3: ")
x2 = int(x2)

y2 = input("Expense 4: ")
y2 = int(y2)

#Process
rise = x2 - x1
run = y2 - y1

if run  == 0:
	Expenxe1 = "Unedefined"
elif run == 1:
	print("Are there any othere expenses to log?")

os.system("Welcome")



labr = tk.Label(root, text="raduis")

labr.pack()


entr = tk.Entry(root)
entr.pack()

root = tk.Tk()
#This configurates your root window
root.title("Average of Daily Expenses")

#Step 1: Create or Construct the element 
labr = tk.Label(root, text="Expense 1")


labr.pack()


entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="Expense 2")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()
output.config(state="disabled")



import tkinter as tk


#creating the main window
#To do this we need to call the TK() function
root = tk.Tk()


root.mainloop()




