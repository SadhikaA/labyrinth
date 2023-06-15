from tkinter import * 
import random 
from PIL import ImageTk, Image

root = Tk()       # create root window
root.title("Labyrinth Game")     # root window title and dimension
root.geometry('800x800')   # Set geometry (width x height)
 
# Creating a label widget
label = Label(root, text="Labyrinth Game")
label.grid(row=1, column=1)

# print current path
my_img = ImageTk.PhotoImage(Image.open("dragon.png"))
my_label = Label(image=my_img)
my_label.grid(row=2, column=1)

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

# Execute Tkinter
root.mainloop()
