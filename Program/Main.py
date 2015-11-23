# First draft to check out how tkinter works 

import Tkinter as tk

# Create Root widget to the program
root = tk.Tk()

# Make a child widget that displays text
text = tk.Label(root, text="The Duke Sent Me.")

# fit inside the root widget
text.pack()

# Display window
root.mainloop()
