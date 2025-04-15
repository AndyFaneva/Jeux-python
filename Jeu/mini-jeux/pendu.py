import tkinter as tk
from tkinter import messagebox
import random

class Hangman:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Pendu (Joueur de football célèbre)")
        self.root.resizable(False,False)
        self.words = ["faneva", "neymar", "messi", "ronaldo", "carolus","mbappe"]
        self.word = random.choice(self.words)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        
        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root,width=500,height=0, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)  # Le canvas s'étend sur toute la fenêtre

        # Ajouter un cadre pour les contrôles
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=20)

        self.word_label = tk.Label(self.control_frame, text=self.get_display_word(), font=("Arial", 24))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.control_frame, font=("Arial", 18))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(self.control_frame, text="Deviner", command=self.make_guess, font=("Arial", 18))
        self.guess_button.pack(pady=10)

        self.status_label = tk.Label(self.control_frame, text="", font=("Arial", 18))
        self.status_label.pack(pady=20)

        label1 = tk.Label(text="Joueur de football célèbre", bg="white")
        self.canvas.create_window(10,10, window=label1)

        self.draw_hangman()

    def get_display_word(self):
        display = ''.join([letter if letter in self.guesses else '_' for letter in self.word])
        return ' '.join(display)

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Erreur", "Veuillez entrer une seule lettre.")
            return

        if guess in self.guesses:
            messagebox.showwarning("Erreur", "Vous avez déjà deviné cette lettre.")
            return

        self.guesses.append(guess)

        if guess not in self.word:
            self.attempts += 1

        self.word_label.config(text=self.get_display_word())
        self.draw_hangman()
        self.update_status()

    def draw_hangman(self):
        self.canvas.delete("all")  # Effacer le canvas avant de dessiner
        # Dessiner les différentes parties du pendu en fonction des essais
        if self.attempts >= 1:
            self.canvas.create_line(50, 250, 150, 250)  # Base
        if self.attempts >= 2:
            self.canvas.create_line(100, 250, 100, 50)  # Poteau
        if self.attempts >= 3:
            self.canvas.create_line(100, 50, 200, 50)  # Poutre
        if self.attempts >= 4:
            self.canvas.create_line(200, 50, 200, 100)  # Crochet
        if self.attempts >= 5:
            self.canvas.create_oval(180, 100, 220, 140)  # Tête
        if self.attempts >= 6:
            self.canvas.create_line(200, 140, 200, 200)  # Corps
            self.canvas.create_line(200, 160, 170, 180)  # Bras gauche
            self.canvas.create_line(200, 160, 230, 180)  # Bras droit
            self.canvas.create_line(200, 200, 170, 230)  # Jambe gauche
            self.canvas.create_line(200, 200, 230, 230)  # Jambe droite

    def update_status(self):
        if self.attempts >= self.max_attempts:
            self.status_label.config(text="Perdu ! Le mot était: " + self.word)
            self.guess_button.config(state=tk.DISABLED)
        elif all(letter in self.guesses for letter in self.word):
            self.status_label.config(text="Gagné ! Vous avez trouvé le mot.")
            self.guess_button.config(state=tk.DISABLED)
        else:
            self.status_label.config(text=f"Essais restants: {self.max_attempts - self.attempts}")

if __name__ == "__main__":
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()
