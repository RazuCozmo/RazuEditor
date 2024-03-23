import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("Practice with Grid")
root.geometry("210x180")  # set starting size of window

def display_checked():
    '''check if the checkbuttons have been toggled, and display
    a value of '1' if they are checked, '0' if not checked'''
    red = red_var.get()
    yellow = yellow_var.get()
    green = green_var.get()
    blue = blue_var.get()

    print("red: {}\nyellow:{}\ngreen: {}\nblue: {}".format(
        red, yellow, green, blue))

# Create label
label = ttk.Label(root, text="Which colors do you like below?")
label.grid(row=0,column=2)

photo = tk.PhotoImage(file = "cube/base.png")
photoimage = photo.subsample(1, 2)

cubeimage = ttk.Label(root, image=photoimage, width=64)
cubeimage.grid(row=0,column=1)

# Create variables and checkbuttons
red_var = tk.IntVar()
ttk.Checkbutton(root, width=10, text="red", variable=red_var).grid(row=1,column=2)

yellow_var = tk.IntVar()
ttk.Checkbutton(root, width=10, text="yellow", variable=yellow_var).grid(row=2,column=2)

green_var = tk.IntVar()
ttk.Checkbutton(root, width=10, text="green", variable=green_var).grid(row=3,column=2)

blue_var = tk.IntVar()
ttk.Checkbutton(root, width=10, text="blue", variable=blue_var).grid(row=4,column=2)

# Create Buttons, one to check which colors are checked,
# and another to close the window.
ttk.Button(root, text="Tally", command=display_checked).grid(row=5,column=2)
ttk.Button(root, text="End", command=root.quit).grid(row=6,column=2)

root.mainloop()