import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Puissance4:
    def __init__(self, root):
        self.root = root
        self.root.title("Puissance 4")
        self.current_player = "Rouge"
        self.root.resizable(False, False)
        self.board = [[None for _ in range(7)] for _ in range(6)]

        self.load_images()
        self.create_buttons()
        self.create_board()

    def load_images(self):
        try:
            # Chargez l'image du bouton
            self.button_image = ImageTk.PhotoImage(Image.open("assets/bouclier.png").resize((40, 40)))
        except Exception as e:
            print(f"Erreur lors du chargement de l'image: {e}")
            self.button_image = None

    def create_buttons(self):
        for i in range(7):
            button = tk.Button(self.root, image=self.button_image, command=lambda col=i: self.drop_piece(col), borderwidth=0)
            button.grid(row=0, column=i, padx=5, pady=5)  # Ajoutez un espacement

    def create_board(self):
        self.board_canvas = tk.Canvas(self.root, width=350, height=300, bg="blue", highlightthickness=0)
        self.board_canvas.grid(row=1, columnspan=7)

    def drop_piece(self, col):
        for row in reversed(range(6)):
            if self.board[row][col] is None:
                self.board[row][col] = self.current_player
                x = 50 + col * 50
                y = 250 - (row * 50)  # Ajustez cette valeur pour bien centrer les cercles
                color = "red" if self.current_player == "Rouge" else "yellow"
                # Dessiner le rond
                self.board_canvas.create_oval(x - 20, y, x + 20, y + 50, fill=color, outline='black')
                if self.check_winner():
                    messagebox.showinfo("Gagnant", f"Le joueur {self.current_player} a gagné !")
                    self.reset_game()
                elif all(self.board[r][c] is not None for r in range(6) for c in range(7)):
                    messagebox.showinfo("Match nul", "Le jeu est un match nul !")
                    self.reset_game()
                else:
                    self.current_player = "Jaune" if self.current_player == "Rouge" else "Rouge"
                break

    def check_winner(self):
        for r in range(6):
            for c in range(7):
                if self.board[r][c] is not None:
                    if self.check_direction(r, c, 1, 0) or self.check_direction(r, c, 1, 1) or \
                       self.check_direction(r, c, 0, 1) or self.check_direction(r, c, 1, -1):
                        return True
        return False

    def check_direction(self, r, c, dr, dc):
        count = 0
        for i in range(4):
            if 0 <= r + i * dr < 6 and 0 <= c + i * dc < 7:
                if self.board[r + i * dr][c + i * dc] == self.board[r][c]:
                    count += 1
                else:
                    break
            else:
                break
        return count == 4

    def reset_game(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.board_canvas.delete("all")  # Effacez tous les cercles
        self.current_player = "Rouge"

if __name__ == "__main__":
    root = tk.Tk()
    game = Puissance4(root)
    root.mainloop()
