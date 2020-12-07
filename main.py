import tkinter as tk
import csv

# import this.classifiers

from tree import regress_Tree, classify_Tree

# Set window elements

# Window for buttons
window = tk.Tk()
window.title("Descision tree classifier")

# Window for table
root = tk.Tk()
root.title("stores.csv")


## LOOP FOR CSV
# open file
with open("stores.csv", newline="") as file:
    reader = csv.reader(file)
    r = 0
    for col in reader:
        c = 0
        for row in col:
            label = tk.Label(
                root, width=10, height=2, text=row, relief=tk.RIDGE
            )
            label.grid(row=r, column=c)
            c += 1
        r += 1


# Window elements

lbl_head = tk.Label(
    text="Hello! Welcome to this small decision tree classifier",
    bg="white",
    height=2,
    master=window,
)

lbl_option = tk.Label(
    text="Please Choose an option:", bg="white", height=2, master=window
)

btn_normal = tk.Button(
    text="Normal Decision Tree", width=25, height=3, bg="#eee9e9", command=classify_Tree
)

btn_regres = tk.Button(
    text="Regression Decision Tree",
    width=25,
    height=3,
    bg="#eee9e9",
    command=regress_Tree,
)


# Creating the window elements


lbl_head.pack(fill=tk.X)
lbl_option.pack(fill=tk.X)
btn_normal.pack(side=tk.LEFT)
btn_regres.pack(side=tk.RIGHT)
# looping the window to responde events and handlers


window.mainloop()