import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time


class PierreFeuilleCiseauxLoterie:
    def __init__(self, root):
        self.root = root
        self.root.title("Pierre-Feuille-Ciseaux")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        # Options de jeu
        self.choices = ["Pierre", "Feuille", "Ciseaux"]
        self.images = {}  # Stockera les images
        self.charger_images()

        # Variables pour suivre les scores et le nombre de tours
        self.score_utilisateur = 0
        self.score_ordinateur = 0
        self.tours_joues = 0
        self.tours_max = 5

        # Variables pour les noms
        self.nom_utilisateur = None
        self.nom_ordinateur = "Tommy"

        # Initialisation du nom du joueur
        self.obtenir_nom_utilisateur()

        # Création des widgets
        self.creer_widgets()

    def charger_images(self):
        """Charge les images pour les choix et le point d'interrogation."""
        self.images["Pierre"] = ImageTk.PhotoImage(Image.open("assets/pierre.png").resize((120, 120)))
        self.images["Feuille"] = ImageTk.PhotoImage(Image.open("assets/feuille.png").resize((120, 120)))
        self.images["Ciseaux"] = ImageTk.PhotoImage(Image.open("assets/ciseaux.png").resize((120, 120)))
        self.images["Question"] = ImageTk.PhotoImage(Image.open("assets/question.png").resize((120, 120)))

    def obtenir_nom_utilisateur(self):
        """Demande le nom du joueur avant de commencer le jeu."""
        nom_fenetre = tk.Toplevel(self.root)
        nom_fenetre.title("Nom du joueur")
        nom_fenetre.geometry("300x150")
        nom_fenetre.resizable(False, False)

        tk.Label(nom_fenetre, text="Entrez votre nom :", font=("Helvetica", 12)).pack(pady=10)
        nom_entry = tk.Entry(nom_fenetre, font=("Helvetica", 12))
        nom_entry.pack(pady=5)

        def definir_nom():
            self.nom_utilisateur = nom_entry.get().strip()
            if not self.nom_utilisateur:
                self.nom_utilisateur = "Joueur"
            nom_fenetre.destroy()

        tk.Button(nom_fenetre, text="OK", font=("Helvetica", 12), command=definir_nom).pack(pady=10)
        self.root.wait_window(nom_fenetre)

    def creer_widgets(self):
        """Crée les éléments de l'interface utilisateur."""
        # Score
        self.score_label = tk.Label(
            self.root, text=f"{self.nom_utilisateur} : 0 | {self.nom_ordinateur} : 0", font=("Helvetica", 12)
        )
        self.score_label.pack(pady=10)

        # Cadres pour afficher les images des joueurs
        frame_images = tk.Frame(self.root)
        frame_images.pack(pady=20)

        # Case du joueur
        self.utilisateur_label = tk.Label(frame_images, image=self.images["Question"])
        self.utilisateur_label.pack(side="left", padx=50)

        # Case de l'ordinateur
        self.ordinateur_label = tk.Label(frame_images, image=self.images["Question"])
        self.ordinateur_label.pack(side="right", padx=50)

        # Boutons pour les choix
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=20)

        tk.Button(frame_buttons, text="Pierre", font=("Helvetica", 12), command=lambda: self.jouer_tour("Pierre")).pack(
            side="left", padx=10
        )
        tk.Button(frame_buttons, text="Feuille", font=("Helvetica", 12), command=lambda: self.jouer_tour("Feuille")).pack(
            side="left", padx=10
        )
        tk.Button(frame_buttons, text="Ciseaux", font=("Helvetica", 12), command=lambda: self.jouer_tour("Ciseaux")).pack(
            side="left", padx=10
        )

    def jouer_tour(self, choix_utilisateur):
        """Joue un tour avec animation de défilement."""
        if self.tours_joues >= self.tours_max:
            messagebox.showinfo("Partie terminée", "La partie est terminée. Cliquez sur Réinitialiser pour recommencer.")
            return

        # Choix de l'ordinateur
        choix_ordinateur = random.choice(self.choices)

        # Affiche le choix de l'utilisateur sans animation
        self.utilisateur_label.config(image=self.images[choix_utilisateur])

        # Animation de défilement pour l'ordinateur
        self.animer_choix_ordinateur(choix_utilisateur, choix_ordinateur)

        # Calcul du résultat
        resultat = self.obtenir_resultat(choix_utilisateur, choix_ordinateur)

        # Mise à jour des scores en fonction du résultat
        if resultat == "Gagné":
            self.score_utilisateur += 1
        elif resultat == "Perdu":
            self.score_ordinateur += 1

        # Mettre à jour le score
        self.tours_joues += 1
        self.score_label.config(text=f"{self.nom_utilisateur} : {self.score_utilisateur} | {self.nom_ordinateur} : {self.score_ordinateur}")

        # Vérifier si la partie est terminée
        if self.tours_joues == self.tours_max:
            self.fin_partie()

    def animer_choix_ordinateur(self, choix_utilisateur, choix_ordinateur):
        """Anime le défilement du choix de l'ordinateur avant de montrer le résultat."""
        for _ in range(10):  # 10 itérations pour l'animation
            choix_ordinateur_aleatoire = random.choice(self.choices)
            self.ordinateur_label.config(image=self.images[choix_ordinateur_aleatoire])
            self.root.update()
            time.sleep(0.1)  # Pause pour l'animation

        # Affiche le choix final de l'ordinateur
        self.ordinateur_label.config(image=self.images[choix_ordinateur])

        # Affiche un message de félicitations ou de consolation
        if self.obtenir_resultat(choix_utilisateur, choix_ordinateur) == "Gagné":
            self.afficher_message("Félicitations", f"{self.nom_utilisateur}, vous avez gagné ! 🎉")
        else:
            self.afficher_message("Désolé", f"Oops ! {self.nom_utilisateur}, vous avez perdu. 😞")

    def obtenir_resultat(self, choix_utilisateur, choix_ordinateur):
        """Détermine le résultat du tour (gagné, perdu ou égalité)."""
        if choix_utilisateur == choix_ordinateur:
            return "Égalité"
        elif (choix_utilisateur == "Pierre" and choix_ordinateur == "Ciseaux") or \
             (choix_utilisateur == "Feuille" and choix_ordinateur == "Pierre") or \
             (choix_utilisateur == "Ciseaux" and choix_ordinateur == "Feuille"):
            return "Gagné"
        else:
            return "Perdu"

    def afficher_message(self, titre, message):
        """Affiche un message avec animation."""
        messagebox.showinfo(titre, message)

    def fin_partie(self):
        """Affiche le gagnant à la fin des 5 tours."""
        if self.score_utilisateur > self.score_ordinateur:
            gagnant = f"{self.nom_utilisateur} a gagné la partie ! 🎉"
        elif self.score_utilisateur < self.score_ordinateur:
            gagnant = f"{self.nom_ordinateur} a gagné la partie. 😞"
        else:
            gagnant = "C'est une égalité générale ! 😐"

        messagebox.showinfo("Partie terminée", f"{gagnant}\nScore final : {self.score_utilisateur} - {self.score_ordinateur}")
        self.reinitialiser_jeu()

    def reinitialiser_jeu(self):
        """Réinitialise le jeu."""
        self.score_utilisateur = 0
        self.score_ordinateur = 0
        self.tours_joues = 0
        self.score_label.config(text=f"{self.nom_utilisateur} : 0 | {self.nom_ordinateur} : 0")
        self.utilisateur_label.config(image=self.images["Question"])
        self.ordinateur_label.config(image=self.images["Question"])


# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = PierreFeuilleCiseauxLoterie(root)
    root.mainloop()
