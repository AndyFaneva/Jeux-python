import tkinter as tk
import random
from PIL import Image, ImageTk

class DinosaurGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Dinosaure")
        self.level = 1
        self.is_game_over = False

        
        self.setup_ui()
        self.setup_game()

    def setup_ui(self):
        # Barre de navigation
        self.nav_frame = tk.Frame(self.root)
        self.nav_frame.pack(side=tk.TOP, fill=tk.X)

        self.level_label = tk.Label(self.nav_frame, text="Choisir le niveau:")
        self.level_label.pack(side=tk.LEFT)

        self.level_var = tk.IntVar(value=1)
        for i in range(1, 4):
            tk.Radiobutton(self.nav_frame, text=f"Niveau {i}", variable=self.level_var, value=i).pack(side=tk.LEFT)

        self.restart_button = tk.Button(self.nav_frame, text="Redémarrer", command=self.restart_game)
        self.restart_button.pack(side=tk.LEFT)

        # Canvas pour le jeu
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.pack()

        self.dino = self.canvas.create_rectangle(50, 300, 100, 350, fill="green")
        self.cacti = []
        self.score = 0
        self.is_jumping = False

    def setup_game(self):
        self.is_game_over = False
        self.score = 0
        self.cacti.clear()
        self.canvas.delete("all")
        self.dino = self.canvas.create_rectangle(50, 300, 100, 350, fill="green")
        self.create_cactus()
        self.update_game()
        self.root.bind("<space>", self.jump)

    def create_cactus(self):
        x = 800
        height = random.randint(20, 70)
        cactus = self.canvas.create_rectangle(x, 350 - height, x + 20, 350, fill="brown")
        self.cacti.append(cactus)

    def update_game(self):
        for cactus in self.cacti:
            self.canvas.move(cactus, -5 - (self.level - 1) * 2, 0)  # Vitesse augmentée selon le niveau

            if self.canvas.coords(cactus)[2] < 0:
                self.canvas.delete(cactus)
                self.cacti.remove(cactus)
                self.score += 1

        if random.random() < 0.02 / self.level:  # Fréquence de création de cactus
            self.create_cactus()

        self.check_collision()
        if not self.is_game_over:
            self.root.after(50, self.update_game)

    def jump(self, event):
        if not self.is_jumping and not self.is_game_over:
            self.is_jumping = True
            self.jump_animation()

    def jump_animation(self):
        for _ in range(20):
            self.canvas.move(self.dino, 0, -5)
            self.root.update()
            self.root.after(20)

        for _ in range(20):
            self.canvas.move(self.dino, 0, 5)
            self.root.update()
            self.root.after(20)

        self.is_jumping = False

    def check_collision(self):
        dino_coords = self.canvas.coords(self.dino)
        for cactus in self.cacti:
            cactus_coords = self.canvas.coords(cactus)
            if (dino_coords[2] > cactus_coords[0] and dino_coords[0] < cactus_coords[2] and
                dino_coords[3] > cactus_coords[1]):
                self.game_over()

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(400, 200, text="Game Over!", font=("Arial", 30), fill="red")
        self.root.unbind("<space>")

    def restart_game(self):
        self.level = self.level_var.get()
        self.setup_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = DinosaurGame(root)
    root.mainloop()
