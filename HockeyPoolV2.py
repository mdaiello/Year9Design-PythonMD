
from tkinter import*
from tkinter import messagebox
from tkinter import filedialog
import requests 

from bs4 import BeautifulSoup


#Imprting tkinter for code
def updatelab():
	lstprint = ""
	for item in lst:
		lstprint = lstprint + item + "\n"
	mylab.configure(text=lstprint)
#definig updatelab() and assigning lstprint
def addItem():
	item = entry.get()
	if (lst.count(item) == 0):
		lst.append(item)
		entry.delete(0, END)
		updatelab()
#defining addItem()

def removeItem():
	item = entry.get()
	if (lst.count(item) > 0):
		lst.remove(item)
		entry.delete(0, END)
		updatelab()

def saveList():
	myfile = open("myplayers.txt", "w")
	for player in lst:
		myfile.writer(player + "\n")
	myfile.close()
	messagebox.showinfo("myplayers.txt", "Congratulations! Your NHL players have been saved to your disk")

def scrape():
	if (messagebox.askyesno("Wait, You must have time, let's wait a few seconds together?") == False):
		return
	if site.status_code is 200:
		content = BeautifulSoup(site.content, 'html.parser')
		totalpts = 0
		for myplayer in lst: #loop to check players
			dTag = content.find(atttrs={"csk": myplayer})
			parent = dTag.findParent('tr')
			playerpts = int(parent.contents[8].text) #8th leg of total points in hockey pool
			print(myplayer + " " + str(playerpts))
			totalpts = totalpts + playerpts
		mypts.configure(text=totalpts)

#this is defining delete, which will be used in the code below

lst = []
lstprint = ""

root = Tk()
root.geometry("300x400+0+900")
root.title("hockey pool")
#adding a root, and telling the computer what the dimensions of the button and Labels that appear in our code 
instlab = Label(root,text="Input (e.g., Mcdavid,Connor): ")
instlab.pack()
#packing and creating a Label
entry = Entry(root)
entry.pack()
#Packing and entry label, which would alow the user to enter something
addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()
#We are adding and packing a button
mylab = Label(root, text=lstprint,anchor=W,justify=LEFT)
mylab.pack()
#Adding a label and packing it which will serve as a root in our program

instlab = Label(root,text="Input (Players List: ")
instlab.pack()

delbutton = Button(root, text="Delete", command=removeItem)
delbutton.pack()
#This is adding a button which is to delete an item when pressed

root.config(background="silver")

savebutton = Button(root, text="Save", command=saveList)
savebutton.pack()

lst = []
lstprint = ""
totalpts = 0
print("Downloading the upmost best hockey data, for you wonderful hockey fans....")


site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')


mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
mylab.pack()

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.pack()

mypts = Label(root, text=totalpts)
mypts.pack()

mainloop()





