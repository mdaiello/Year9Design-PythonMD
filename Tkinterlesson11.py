
#importing tkinter module into python so we can use it
from tkinter import * #1
# Tk() makes a window
master = Tk() #1


# Create this method before you create the entry
def return_entry(en):

	"""Gets and prints te content of the entry"""
	coment = entry.get()
	print(conetent)


Label(master, text="Input:  ").grid(row=1, sticky=W)

entry = Entry(master)
entry.grid(row=0, column=1)


#Connect the entry with the return button
entry.bind('<Return>', return_entry)
#mainloop keeps window open
mainloop()
