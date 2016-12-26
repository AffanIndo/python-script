import tkinter as tk # importing the tkinter package, do not use from unless you need less than ~3 names from the module
root = tk.Tk() # Tk() is creating the window that you see and storing it inside the 'root' variable
root.geometry('300x300') # this is the dimension of the window (optional)
root.title("My Window!") # set the title of the window

label1 = tk.Label(root, text="Hello World!", bg="aqua", fg="black", font="arial, 20")
label1.pack()
label2 = tk.Label(root, text="Hello World!", bg="green", fg="black", font="arial, 20")
label2.pack()

root.mainloop() # make sure the window stays and doesn't disappear
