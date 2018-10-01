def__init__(self):

	self.root = tk.Tk()

	self.root.title("GUI ENTRY - Class")

	self.entry1 = tk.Entry(self.root)

	self.entry1 bind("<Return>", self.onReturn)

	self.entry1.pack()

	self.root.mainloop()

def onReturn(self, events):

	print("Return Pressed")

	value = self.entry1.get()
	self.entyr1.delete(0.'end')

