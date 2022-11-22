from tkinter import *

# create a root window.
top = Tk()

# create listbox object
listbox = Listbox(top, height=10,
                  width=15,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow")

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text=" FOOD ITEMS")

#let's try to read in some car_data.txt
file = open("car_data.txt", "r")
lines = file.readlines()
for index in range(len(lines)):
    if "black" in lines[index]:
        listbox.insert(index, lines[index])

# insert elements by their
# index and names.
# listbox.insert(1, "Nachos")
# listbox.insert(2, "Sandwich")
# listbox.insert(3, "Burger")
# listbox.insert(4, "Pizza")
# listbox.insert(5, "Burrito")

# pack the widgets
label.pack()
listbox.pack()

# Display until User
# exits themselves.
top.mainloop()