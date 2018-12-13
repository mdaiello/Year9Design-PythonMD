def switchPhoto():
	global photo
	myimage = Image.open("headshots/kesseph01.jpg")
	photo = ImageTk.PhotoImage(my_image)
	can.itemconfig(myimg, image=photo)

root = Tk()
root.geometry()
root.title("hockey pool")

can = Canavas(root, width=125, height=180)
image1 = Image.open("headshots/marnemi.jpg")
photo = ImageTk.PhotoImage(image1)
myimg = can.create_image(0, 0, anchor=Nw, image=photo)
can.pack()


button = Button(root, text="Change photo", command=switchPhoto)
button.pack()
