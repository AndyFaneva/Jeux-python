import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = [None] * 9
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            self.buttons[i] = tk.Button(self.root, text=" ", font="Arial 20", width=5, height=2,
                                         command=lambda i=i: self.make_move(i))
            self.buttons[i].grid(row=i // 3, column=i % 3)

    def make_move(self, i):
        if self.board[i] == " ":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.current_player == "X":
                self.buttons[i].config(fg="red")  # Couleur rouge pour X
            else:
                self.buttons[i].config(fg="blue")  # Couleur bleue pour O
            
            if self.check_winner():
                messagebox.showinfo("Gagnant", f"Le joueur {self.current_player} a gagné !")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Match nul", "Le jeu est un match nul !")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
            [0, 4, 8], [2, 4, 6]               # Diagonales
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", fg="black")  # Réinitialisez la couleur
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
