import tkinter as tk
from PIL import Image, ImageTk

class Apropos:
    def __init__(self,root):
        self.root = root
        self.root.title("A propos")
        self.root.resizable(False,False)

        self.canvas=tk.Canvas(root,width=500,height=250,bg="blue")
        self.canvas.pack(fill="both", expand=True)

        label = tk.Label(text="A propos du Jeux", bg="yellow")
        self.canvas.create_window(250,20,window=label)

        label = tk.Label(text="Lorem, ipsum dolor sit amet consectetur adipisicing elit.", bg="yellow",width=50)
        self.canvas.create_window(250,60,window=label)
        label1 = tk.Label(text=" Dolor corrupti pariatur, possimus autem consequuntur beatae maxime delectus minima dicta?", bg="yellow",width=50)
        self.canvas.create_window(250,80,window=label1)
        label2 = tk.Label(text="  Dolorum assumenda perferendis iste rem impedit ipsum eos, neque omnis. Ad.", bg="yellow",width=50)
        self.canvas.create_window(250,100,window=label2)
        label3 = tk.Label(text="Lorem, ipsum dolor sit amet consectetur adipisicing elit.", bg="yellow",width=50)
        self.canvas.create_window(250,120,window=label3)
        label4 = tk.Label(text=" Dolor corrupti pariatur, possimus autem consequuntur beatae maxime delectus minima dicta?", bg="yellow",width=50)
        self.canvas.create_window(250,140,window=label4)
        label5 = tk.Label(text="  Dolorum assumenda perferendis iste rem impedit ipsum eos, neque omnis. Ad.", bg="yellow",width=50)
        self.canvas.create_window(250,160,window=label5)


if __name__ == "__main__":
    root = tk.Tk()
    app = Apropos(root)
    root.mainloop()
