from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("420x400+0+900")
root.configure(background="white")
root.title("Hockey Pool")

#draw canvas

'''
can = Canvas(root, width=400, height=225)
can.grid(row=0,column=0,padx=10, pady=10)
image1 = Image.open("sid.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0, 0, anchor=NW, image=photo)

can.create_oval(325, 25, 375, 75, fill="black", outline="#DDD", width=4)
can.create_line(250, 50, 320, 50, fill="#DDD", width=4)
can.create_line(275, 40, 320, 40, fill="#DDD", width=4)
can.create_line(275, 60, 320, 60, fill= "#DDD", width=4)
'''
#listbox
listbox = Listbox(root,height=7)
listbox.grid(row=1,column=0, sticky=M, padx=10)
listbox.insert(END, "Crosby,Sidney")


#pulldown

OPTIONS = ["Crosby,Sidney", "McDavid,Connor"]
variable = StringVar(root)
variable.set(OPTIONS[0]) #default value
w = OptionMenu(root, variable, *OPTIONS)
w.grid(row=1, column=0, sticky=NE,padx=10)

#button
savebutton = Button(root, text="Save")
savebutton.grid(row=1, column=0, sticky=E, padx=10)


mainloop()