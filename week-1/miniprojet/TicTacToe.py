import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        
        # Initialisation du plateau
        self.plateau = [" "] * 9
        self.joueur_courant = "X"
        self.tours = 0
        
        # Frame principale
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(padx=10, pady=10)
        
        # Création des boutons du plateau
        self.boutons = []
        for i in range(9):
            bouton = tk.Button(self.main_frame, text=" ", font=("Arial", 20), width=5, height=3,
                             command=lambda x=i: self.cliquer(x))
            bouton.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.boutons.append(bouton)
        
        # Bouton reset
        self.reset_btn = tk.Button(self.main_frame, text="Rejouer", command=self.reinitialiser,
                                 font=("Arial", 12))
        self.reset_btn.grid(row=3, column=0, columnspan=3, pady=10)
        
        # Label du joueur courant
        self.label_joueur = tk.Label(self.main_frame, text="Tour du joueur X",
                                   font=("Arial", 12), bg="#f0f0f0")
        self.label_joueur.grid(row=4, column=0, columnspan=3)

    def cliquer(self, position):
        """Gère le clic sur une case."""
        if self.plateau[position] == " " and self.tours < 9:
            self.plateau[position] = self.joueur_courant
            self.boutons[position].config(text=self.joueur_courant)
            self.tours += 1
            
            if self.verifier_gagnant():
                messagebox.showinfo("Victoire", f"Le joueur {self.joueur_courant} a gagné !")
                self.desactiver_boutons()
            elif self.tours == 9:
                messagebox.showinfo("Égalité", "Match nul !")
            else:
                self.joueur_courant = "O" if self.joueur_courant == "X" else "X"
                self.label_joueur.config(text=f"Tour du joueur {self.joueur_courant}")

    def verifier_gagnant(self):
        """Vérifie s'il y a un gagnant."""
        combinaisons_gagnantes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
            [0, 4, 8], [2, 4, 6]              # diagonales
        ]
        
        for combinaison in combinaisons_gagnantes:
            if (self.plateau[combinaison[0]] == self.plateau[combinaison[1]] == 
                self.plateau[combinaison[2]] != " "):
                # Colorier les cases gagnantes
                for pos in combinaison:
                    self.boutons[pos].config(bg="#90ee90")
                return True
        return False

    def desactiver_boutons(self):
        """Désactive tous les boutons après la fin du jeu."""
        for bouton in self.boutons:
            bouton.config(state="disabled")

    def reinitialiser(self):
        """Réinitialise le jeu."""
        self.plateau = [" "] * 9
        self.joueur_courant = "X"
        self.tours = 0
        self.label_joueur.config(text="Tour du joueur X")
        for bouton in self.boutons:
            bouton.config(text=" ", state="normal", bg="SystemButtonFace")

    def jouer(self):
        """Démarre le jeu."""
        self.root.mainloop()

# Lancer le jeu
if __name__ == "__main__":
    jeu = TicTacToe()
    jeu.jouer()