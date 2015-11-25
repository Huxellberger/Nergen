# First draft to check out how tkinter works 
# Uses a grid layout
import Tkinter as tk


class NergenWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.UIGen()

    # Create the U.I
    def UIGen(self):
        self.master.title("Nergen Character Generator")
        introLabel = tk.Label(self, 
                     text="The Duke sent me.").grid(row=0)
        race = tk.StringVar()
        tk.Radiobutton(self, text="Human", variable=race, 
         value="Human").grid(row=1, column=0, sticky=tk.W) 
        tk.Radiobutton(self, text="Elf", variable=race,
         value="Elf").grid(row=1, column=1, sticky=tk.W) 
        tk.Radiobutton(self, text="Dwarf", variable=race,
         value="Dwarf").grid(row=1, column=2, sticky=tk.W) 
        tk.Radiobutton(self, text="Half Elf", variable=race,
         value="Half Elf").grid(row=1, column=3, sticky=tk.W) 

        name = tk.Entry(self)
        nameLabel = tk.Label(self, text="Enter Name").grid(row=2, column=0)
        name.grid(row=2, column=1)
    # Sticky aligns grid either N,E,S or west above. Default centre


def main():
  root = tk.Tk()
  NergenWindow(root).pack()
  root.mainloop()

main()




