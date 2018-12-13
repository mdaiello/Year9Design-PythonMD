import tkinter as tk 
import math

def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)
	output.config(state="normal")

	output.config(state="normal")

	output.delete(1.0,tk.END)
	outputValue = " Given Amounts\nraduis: "+str(r)+" units\nheight: "+str(h)+" units\nThe volume is: "+str(v)+ " units cubed \n\n "
	output.insert(tk.INSERT,outputValue)
	output.config(state="disabled")


#This constructs your root window
root = tk.Tk()
#This configurates your root window
root.title("Volume of a Cylinder")

#Step 1: Create or Construct the element 
labr = tk.Label(root, text="raduis")


labr.pack()


entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()
output.config(state="disabled")







#This start your EVENT DRIVEN PROGRAM
#The terminal is waiting for you to start or enter things into the program
root.mainloop()
print("END PROGRAM")