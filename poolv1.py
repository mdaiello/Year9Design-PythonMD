

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup


lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
  content = BeautifulSoup(site.content, 'html.parser')
else:
  content != -99

print("Your amazing NHL Hockey Pool awaites, So wait when its loading....")


def viewItem():
   
   
    var = entry.get()
    playerstats = ""
    
    
    content = BeautifulSoup(site.content, 'html.parser')           
    
    dTag=content.find(attrs={"csk":var})
    if site.status_code is 200 and dTag!=NONE:    
        parent=dTag.findParent("tr")
        points=int(parent.contents[8].text)
        games=int(parent.contents[5].text)
        team=str(parent.contents[3].text)
        position=str(parent.contents[4].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        
        listbox2=Listbox(root, background="light grey")
        listbox2.place(x=1000,y=500)
        
        listbox2.insert(END, "Games Played: " + str(games))
        listbox2.insert(END,"Points: " + str(points))
        listbox2.insert(END,"Team: " + team)
        listbox2.insert(END,"Position: " + position)
        listbox2.insert(END,"Goals: " + str(goals))
        listbox2.insert(END,"Assists: " + str(assists))
    

def restartItem():
    listbox2=Listbox(root)
    listbox2.place(x=200,y=210)
    mylab=Listbox(root,height=10)
    mylab.place(x=400,y=210)
    entry.delete(0, END) 

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
      

def listboxcreate(value):
	var=listbox.get(ANCHOR)
	if var!=NONE:
		dTag = content.find(attrs={"csk": myplayer})
		parent = dTag.findParent('tr')
		points = int(parent.contents[8].text) #
		listbox2=Listbox(root)
		listbox2.grid(row=1, column=2, sticky=W, padx=10)
		listbox2=listbox.insert(END,"Points: ",str(points))

def addValue(value):
  if (lst.count(value) == 0):
    lst.append(value)
    listbox.insert(END, value)

def switchPhoto():
  fullname = listbox.get(ACTIVE)
  full_list = fullname.split(",")
  first = full_list[1]
  last = full_list[0]
  filename = "headshots/" + last [0:5] + first[0:2] 


def saveList():
    myfile = open("myplayers.txt","w")
    lst = []
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Your NHL Players have been saved to disk")

def scrape():
    if (messagebox.askyesno("You look like you have some time, let's wait") == False):
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


#global photo
#myimage = Image.open("headshots/kesseph01.jpg")
#photo3 = ImageTk.PhotoImage(my_image)
#can.itemconfig(myimg, image=photo)
  #my_image = Image("headshots/marnemi01.jpg")

def makeList():
  if content !=-99:
        names=content.findAll(attrs={"data-stat":"player"})
        for player in names:
            if (player.get("csk")!=None or player.get("csk")!=""):
                playerlist.append(player.get('csk'))
        return playerlist


#root = Tk()
#root.geometry("300x400+0+900")
#root.title("hockey pool")


#draw canvas
root = Tk()
root.geometry("5000x2000+0+5000")
root.configure(background="blue")
root.title("Your Personal NHL Hockey Pool")


can = Canvas(root, width=400, height=225, background="dark blue")
can.place(x=275,y=175)
image1 = Image.open("nhl.jpg")
photo = ImageTk.PhotoImage(image1)
myimg = can.create_image(0, 0, anchor=NW, image=photo)


can2 = Canvas(root, width=400, height=225, background="dark blue")
can2.place(x=800, y=175)
image2 = Image.open("cool.jpg")
photo2 = ImageTk.PhotoImage(image2)
myimg = can2.create_image(0, 0, anchor=NW, image=photo2)

can.create_oval(325, 25, 375, 75, fill="black", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 40, 320, 40, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill= "#DDD", width=4)



#listbox
listbox = Listbox(root,height=7)


#pulldown



#button

#print(my_image)

root.config(background="dark blue")


instlab = Label(root,text="Input Player Name Below (e.g., McDavid,Connor)", background="red")
instlab.place(x=400,y=450)
instlab.config(font=("Courier", 25))

mylab = Label(root,text="Welcome to Your Personal Hockey Pool", background="light grey")
mylab.place(x=200,y=70)
mylab.config(font=("Courier", 50))


entry = Entry(root)     
entry.place(x=575,y= 500, height=50)
entry.config(font=("Courier", 25))

listbox.bind('<<LisboxSelect>>',listboxcreate)
listbox.bind("<Double-Button-1>", remItem)

mylab = Label(root,text=lstprint,anchor=W,justify=LEFT, background="red")
mylab.place(x=325,y=500)
mylab.config(font=("Courier", 15))

savebutton = Button(root, text="Save", command=saveList, background="red")
savebutton.place(x=950,y=700)
savebutton.config(font=("Courier", 15))

addbutton = Button(root, text="Add Players to List", command=addItem, background="red")
addbutton.place(x=500,y=700)
addbutton.config(font=("Courier", 15))

rembutton = Button(root, text="Remove Players from List", command=remItem, background="red")
rembutton.place(x=700,y=700)
rembutton.config(font=("Courier", 15))

viewbutton = Button(root,text="View Stats", command=viewItem, background="red")
viewbutton.place(x=650,y=575)
viewbutton.config(font=("Courier", 25))

mypts = Label(root,text=totalpts, background="red")
mypts.place(x=450,y=600)
mypts.config(font=("Courier", 15))

ptsbutton = Button(root,text="Total Points", command=scrape, background="red")
ptsbutton.place(x=325,y=600)
ptsbutton.config(font=("Courier", 15))

mainloop()
