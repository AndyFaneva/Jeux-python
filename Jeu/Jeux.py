import random
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class Jeux:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeux")
        self.root.resizable(False,False)

        self.bg_image = Image.open("assets/il_570xN.5022632129_kwst.jpg")
        self.bg_image = self.bg_image.resize((500,350))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(root, width=500, height=350)
        self.canvas.pack(fill="both", expand=True)
        
        self.canvas.create_image(0,0, image = self.bg_photo, anchor="nw")

        label = tk.Label(root, text="MINI JEUX VIDÉO", font=("Times new romans",25), bg="white",width=25, height=0)
        self.canvas.create_window(250,35, window=label)

        def PFC():
            subprocess.run(["python","mini-jeux/PFC.py"])
            
        PFC = tk.Button(root, text="Pierre Feuille Ciseau", font=("Helvetica",14),bg="red", command=PFC, width=20,height=0)
        self.canvas.create_window(125,100, window=PFC)

        def Puissance():
            subprocess.run(["python","mini-jeux/P4.py"])
        
        Puissance = tk.Button(root, text="Puissance Quatre", font=("Helvetica", 14),bg="red", command=Puissance, width=20,height=0)
        self.canvas.create_window(125,150, window=Puissance)

        def Snake():
            subprocess.run(["python","mini-jeux/snake.py"])

        Snake = tk.Button(root, text="Serpent", font=("Helvetica", 14), bg="red", command=Snake, width=20,height=0)
        self.canvas.create_window(125,200, window=Snake)

        def Tictac():
            subprocess.run(["python","mini-jeux/TicTac.py"])

        Tictac = tk.Button(root, text="Tic Tac Toe", font=("Helvetica", 14), bg="red", command=Tictac, width=20,height=0)
        self.canvas.create_window(375,100, window=Tictac)

        def Pendu():
            subprocess.run(["python","mini-jeux/Pendu.py"])

        Pendu = tk.Button(root, text="Pendu", font=("Helvetica", 14), bg="red", command=Pendu, width=20,height=0)
        self.canvas.create_window(375,150, window=Pendu)

        def Dino():
            subprocess.run(["python","mini-jeux/dino.py"])

        Dino = tk.Button(root, text="Dinosaure", font=("Helvetica", 14), bg="red", command=Dino, width=20,height=0)
        self.canvas.create_window(375,200, window=Dino)

        statistique = tk.Button(root, text="Statistique", font=("Helvetica", 14), bg="green")
        self.canvas.create_window(325,325, window=statistique)

        def Apropos():
            subprocess.run(["python","mini-jeux/apropos.py"])
            
        apropos = tk.Button(root, text="A propos", font=("Helveticca", 14), bg="yellow", command=Apropos)
        self.canvas.create_window(440,325, window=apropos)

if __name__ == "__main__":
    root = tk.Tk()
    app = Jeux(root)
    root.mainloop()
