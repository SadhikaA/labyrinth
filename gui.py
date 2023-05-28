from tkinter import * 
import random 

root = Tk()       # create root window
root.title("Labyrinth Game")     # root window title and dimension
root.geometry('800x800')   # Set geometry (width x height)
 
# Creating a label widget
label = Label(root, text="Labyrinth Game")
label.grid(row=1, column=1)

# buttons 
end = Button(root, text="End Game", command=root.quit, fg="red", bg="#FBD5D5")
end.grid(row=2, column=1)

shuffle = Button(root, text="Shuffle Cards")     # command=shuffle_deck
shuffle.grid(row=3, column=0)

# functions 
def shuffle_deck():
    # shuffle deck of cards
    pass

# create frame for cards
card_frame = Frame(root, bg="#FBD5D5", width=600, height=600)
card_frame.grid(row=3, column=3, rowspan=4, columnspan=4)
card_label = Label(card_frame, text="Cards", bg="#FBD5D5")

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
