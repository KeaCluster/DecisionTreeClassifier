import tkinter as tk


# import this.classifiers

from tree import regres_Tree, classify_Tree

window = tk.Tk()
window.title("Descision tree classifier")

# Window elements


lbl_head = tk.Label(
    text="Hello! Welcome to this small decision tree classifier",
    bg="white",
    height=2,
    master=window,
)

lbl_option = tk.Label(
    text="Please Choose an option:", 
    bg="white", 
    height=2, 
    master=window
)

btn_normal = tk.Button(
    text="Normal Decision Tree",
    width=25,
    height=3,
    bg="#eee9e9",
    command=classify_Tree
)

btn_regres = tk.Button(
    text="Regression Decision Tree",
    width=25,
    height=3,
    bg="#eee9e9",
    command=regres_Tree,
)


# Creating the window elements


lbl_head.pack(fill=tk.X)
lbl_option.pack(fill=tk.X)
btn_normal.pack(side=tk.LEFT)
btn_regres.pack(side=tk.RIGHT)
# looping the window to responde events and handlers


window.mainloop()