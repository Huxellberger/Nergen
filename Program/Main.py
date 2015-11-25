# First draft to check out how tkinter works 

import Tkinter as tk


class GUI(tk.Frame):
  def _init_(self, master):

    # Create the frame to hold the Gooey GUI details
    tk.Frame._init_(self, master)

    self.master = master
    self.initUI()
  

  def initUI(self):

    # self.style = Style()
    # self.style.theme_use("default")
    self.master.title = ("Nergen Character Generator")

    # self.pack(fill=BOTH, expand=1)
 
    # Make a button to close the window
    # self.button = tk.Button(self, text="GO AWAY", fg="red", 
    #                         command=self.quit)
    # self.button.place(x=40, y=40)

    # self.greet = tk.Button(self, text="Push Me", command=self.greet)
    # self.greet.place(x=50, y=50)

    # Make a child widget that displays text
    text = tk.Label(self, text="The Duke Sent Me.")
    text.pack()
    

  def greet(self):
    print "Greetings!!" 


def main():
  # Create Root widget to the program
  root = tk.Tk()
  gui = GUI(root)

  # Display window
  root.mainloop()

  # Include destroy to make sure main window lost on close
  root.destroy()

main()




