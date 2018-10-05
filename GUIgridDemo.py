#tkinter is a module that holds all the function
#that let us easily make GUI elements
import tkinter as tk


#creating the main window
#To do this we need to call the TK() function
root = tk.Tk()
label = tk.Label(root, text = "Welcome to Concentration")
label.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root,text ="1")
btn1.config(width = 5, height = 5)
btn1.grid(row = 1, column = 0, sticky = "NESW")

btn2 = tk.Button(root,text ="2")
btn2.config(width = 5, height = 5)
btn2.grid(row = 1, column = 1, sticky = "NESW")


btn3 = tk.Button(root,text ="3")
btn3.grid(row = 2, column = 0, sticky = "NESW")
btn3.config(width = 5, height = 5)


btn4 = tk.Button(root,text ="4")
btn4.grid(row = 2, column = 1, sticky = "NESW")
btn4.config(width = 5, height = 5)


#This line displays the root and sets the program
#in a infinit loop. This is an EVENT DRIVEN PROGRAM

root.mainloop()
#All of this code above generates the window and the comments below  
#imprt tkinter as tk
#root = tk.Tk()
#root.mainloop() 
