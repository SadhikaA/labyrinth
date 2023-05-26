from tkinter import * 
import random 

# create root window
root = Tk()
 
# root window title and dimension
root.title("Labyrinth Game")

# Set geometry (widthxheight)
root.geometry('800x800')
 

# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

#adding a label to the root window
label = Label(root, text = "Rules of the Game")
label.grid()

# Execute Tkinter
root.mainloop()
