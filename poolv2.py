from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

statprint=""
lstprint=""
print("Downloading hockey data")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

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
        
        listbox2=Listbox(root)
        listbox2.place(x=200,y=210)
        
        listbox2.insert(END,"Points: " + str(points))
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
def addItem():
    item = entry.get()
    mylab.insert(END, "\n"+item)
    entry.delete(0, END)
    listbox.configure(text="") 
    listbox2=Listbox(root)
    listbox2.place(x=200,y=210)

def saveList():
    myfile = open("myplayers.txt","w")
    lst = []
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Your NHL Players have been saved to disk")

   
def clearItem():
    statprint=""
    entry.delete(0, END) 
    listbox2=Listbox(root)
    listbox2.place(x=200,y=210)
    
root = Tk()
root.geometry("600x450+0+800")
root.title("hockey pool")

canvas = Canvas(root,width=800,height=200)
canvas.place(x=0,y=0)
image = Image.open("nhl.jpg")
photo=ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=NW, image=photo)

#headshot = Canvas(root,width=260,height=140)
#headshot.place(x=0,y=310)
#headshotimage = Image.open("CornerImage.jpg")
#headshotphoto=ImageTk.PhotoImage(headshotimage)
#headshot.create_image(0, 0, anchor=NW, image=headshotphoto)

instlab = Label(root,text="Input (e.g., McDavid,Connor): ")
instlab.place(x=10,y=210) 

entry = Entry(root)     
entry.place(x=10,y=240)

viewbutton = Button(root, text="View", command=viewItem)
viewbutton.place(x=10,y=270)

clearbutton = Button(root, text="Clear", command=clearItem)
clearbutton.place(x=50,y=270)

savebutton = Button(root, text="Save", command=saveList)
savebutton.place(x=90,y=270)


restartbutton = Button(root, text="Restart", command=restartItem)
restartbutton.place(x=475,y=400)

listbox = Label(root,text=statprint,anchor=W,justify=LEFT)
listbox.place(x=250,y=210)

addbutton = Button(root, text="Add", command=addItem)
addbutton.place(x=280,y=400)

mylab = Listbox(root,height=10)
mylab.place(x=400,y=210)

title = Label(root,text="My players",anchor=W,justify=LEFT)
title.place(x=450,y=180)

mainloop()