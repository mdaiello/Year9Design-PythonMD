from tkinter import*

def updatelab():
	lstprint = ""
	for ite in lst:
		lstprint = lstprint + item + "\n"
	mylab.configure(text=listprint)

def addItem():
	item = entry.get()
	if (lst.count != 0):
		lst.append(item)
		entry.delete(0, END)
		updatelab()

lst = []
lstprint = ""

root = Tk()
root.geometry("300x400+0+900")
root.title("hockey pool")

instlab = Label(root,text="Input (e.g., Mcdavid,Connor:")
instlab.pack()

entry = Entry(root)
entry.pack()

addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()

mylab = Label(root, text=lstprint,anchor=W,justify=LEFT)
mylab.pack()


mainloop()
