from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

print("Your amazing NHL Hockey Pool awaites, So wait when its loading....")

def saveList():
    myfile = open("myplayers.txt","w")
    lst = []
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Your NHL Players have been saved to disk and your hockey pool is ready to start")

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
            content = BeautifulSoup(site.content, 'html.parser')                    
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)

def updatelab():
   lstprint = ""
   for item in lst:
       lstprint = lstprint + item + "\n"
   mylab.configure(text=lstprint) 

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      entry.delete(0, END)
      listbox.delete(listbox.index(ACTIVE)) 
      updatelab()   

def addValue(value):
  if (lst.count(value) == 0):
    lst.append(value)
    listbox.insert(END, value)

def remItem():
   item = entry.get()
   if (len(lst) != 0):
      lst.remove(item)
      entry.delete(0, END) 
      updatelab()

def listboxcreate(value):
	var=listbox.get(ANCHOR)
	if var!=NONE:
		dTag = content.find(attrs={"csk": myplayer})
		parent = dTag.findParent('tr')
		points = int(parent.contents[8].text) #
		listbox2=Listbox(root)
		listbox2.grid(row=1, column=2, sticky=W, padx=10)
		listbox2=listbox.insert(END,"Points: ",str(points))

def remItem():
   item = entry.get()
   if (len(lst) != 0):
      lst.remove(item)
      entry.delete(0, END) 
      updatelab()

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      entry.delete(0, END)
      listbox.delete(listbox.index(ACTIVE)) 
      updatelab()   


def addValue(value):
  if (lst.count(value) == 0):
    lst.append(value)
    listbox.insert(END, value)

def updatelab():
   lstprint = ""
   for item in lst:
       lstprint = lstprint + item + "\n"
   mylab.configure(text=lstprint) 

def createlistbox(value):
    var=listbox.get(ANCHOR)
    if var!=NONE:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        points=int(parent.contents[8].text)
        games=int(parent.contents[5].text)
        team=str(parent.contents[3].text)
        position=str(parent.contents[4].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
    listbox2 = Listbox(root,height=9)
    listbox2.place(x=500, y=309)
    listbox2.insert(END, "[Stats]")
    listbox2.insert(END,"Points: " + str(points))
    listbox2.insert(END, "Games Played: " + str(games))
    listbox2.insert(END,"Team: " + team)
    listbox2.insert(END,"Position: " + position)
    listbox2.insert(END,"Goals: " + str(goals))
    listbox2.insert(END,"Assists: " + str(assists))


root = Tk()

can = Canvas(root, width=400, height=225)
can.grid(row=0,column=0,padx=10, pady=10)
image1 = Image.open("nhl.jpg")
photo = ImageTk.PhotoImage(image1)
myimg = can.create_image(0, 0, anchor=NW, image=photo)


can.create_oval(325, 25, 375, 75, fill="red", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 40, 320, 40, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill= "#DDD", width=4)




#def lstinfo(value):
	#lstprint = ""
	#if len(listbox.curselection()) == 0:
		#lstprint = lst[0]
	#else:
		#lstprint = listbox.get()


root.geometry("850x600+0+900")
root.configure(background="light green")
root.title("Your Personal NHL Hockey Pool")


instlab = Label(root,text="Welcome to your personal hockey pool where you can compete with your friends")
instlab.grid(row=0, column=2, sticky=E, padx=10) 

entry = Entry(root)     
entry.grid(row=2,column=0, sticky=W, padx=10)

savebutton = Button(root, text="Save Players and Start Pool", command=saveList)
savebutton.grid(row=2,column=2, sticky=W, padx=10)

addbutton = Button(root, text="Add Friends to your Hockey Pool", command=addItem)
addbutton.grid(row=1, column=0, sticky=E, padx=10)

rembutton = Button(root, text="Remove", command=remItem)
rembutton.grid(row=2, column=0, sticky=E, padx=10)

instlab = Label(root, text="Time Left till Season Start: 0:00")
instlab.grid(row=1, column=1, sticky=E, padx=10)


mainloop()






