from tkinter import *
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup

def scrape():
    if (messagebox.askyesno("Wait?", "You look like you have some time? Wanna wait with me?") == False):
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
      updatelab()        
            
def remItem():
   item = entry.get()
   if (len(lst) != 0):
      lst.remove(item)
      entry.delete(0, END) 
      updatelab()
      
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Your NHL Players have been saved to disk")
    
def addValue(value):
  if (lst.count(value) == 0):
    lst.append(value)
    listbox.insert(END, value)

def makeList():
  lst = []
lstprint = ""
totalpts = 0
print("Downloading the upmost best hockey data, for you wonderful hockey fans...")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
  content = BeautifulSoup(site.content, 'html.parser')
else:
  content != -99

root = Tk()
root.geometry("300x400+0+900")
root.title("NHL Hockey pool")

instlab = Label(root,text="Input (e.g., McDavid,Connor): ")
instlab.pack() 


root.config(background="silver")


entry = Entry(root)     
entry.pack()

addbutton = Button(root, text="Add", command=addItem)
addbutton.pack()

rembutton = Button(root, text="Remove", command=remItem)
rembutton.pack()

savebutton = Button(root, text="Save", command=saveList)
savebutton.pack()

mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
mylab.pack()

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.pack()

mypts = Label(root,text=totalpts)
mypts.pack()





OPTIONS = makeList()
variable = StringVar(root)
variable.set(OPTIONS)




from tkinter import *
from PIL import ImageTk, Image
print("Your amazing NHL Hockey Pool awaites, So wait when its loading....")





#draw canvas
root = Tk()
root.geometry("850x600+0+900")
root.configure(background="blue")
root.title("Your Personal NHL Hockey Pool")

can = Canvas(root, width=400, height=225)
can.grid(row=0,column=0,padx=10, pady=10)
image1 = Image.open("nhl.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(325, 25, 375, 75, fill="black", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 40, 320, 40, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill= "#DDD", width=4)

#listbox
listbox = Listbox(root,height=7)
listbox.grid(row=2,column=0, sticky=W, padx=10)
listbox.insert(END, "Connor Brown | #28", "Tyler Ennis | #63", "Frederik Gauthier | #33", "Zach Hyman | #11", "Andreas Johnsson | #18", "Nazem Kadri | #43", "Kasperi Kapanen | #24", "Josh Leivo | #32")

#pulldown

OPTIONS = [ "Toronto Maple Leafs", "Carolina Hurricanes", "Columbus Blue Jackets", "New Jersey Devils", "New York Islanders", "New York Rangers", "Philadelphia Flyers", "Pittsburgh Penguins", "Washington Capitals", "Boston Bruins", "Buffalo Sabres", "Detroit Red Wings", "Florida Panthers", "Montréal Canadiens", "Ottawa Senators", "Tampa Bay Lightning", "Chicago Blackhawks", "Colorado Avalanche", "Dallas Stars", "Minnesota Wild", "Nashville Predators", "St. Louis Blues", "Winnipeg Jets", "Anaheim Ducks", "Arizona Coyotes", "Calgary Flames", "Edmonton Oilers", "Los Angeles Kings", "San Jose Sharks", "Vancouver Canucks", "Vegas Golden Knights"]
variable = StringVar(root)
variable.set(OPTIONS[0]) #default value
w = OptionMenu(root, variable, *OPTIONS)
w.grid(row=1, column=0, sticky=NE,padx=10)

#button



root.config(background="blue")

listbox = Listbox(root,height=7)
listbox.grid(row=1,column=2, sticky=W, padx=10)
listbox.insert(END, "Your Players List", "Zach Hyman | #11")

addbutton = Button(root, text="Add player to list")
addbutton.grid(row=1, column=0, sticky=E, padx=10)

addbutton = Button(root, text="Remove player from list")
addbutton.grid(row=2, column=0, sticky=E, padx=10)

addbutton = Button(root, text="Search Statistics")
addbutton.grid(row=1, column=1, sticky=E, padx=10)

addlabel = Label(root, text="Team Roster") 
addlabel.grid(row=1,column=0, sticky=W, padx=10)

savebutton = Button(root, text="Save", command=saveList)
savebutton.grid(row=2,column=2, sticky=W, padx=10)





mainloop()

mainloop()