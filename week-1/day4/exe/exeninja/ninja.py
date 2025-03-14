import os # pour nettoyer l'ecran
import time # sleep time
import tkinter as tk
#bordures fixes
class GameOfLifeFixed:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Initialiser une grille vide 
        self.grid = [[0 for _ in range(width)] for _ in range(height)] # grille 2D interne pour largeur externe pour hauteur

    def set_cell(self, x, y, state):
        """Définir l'état d'une cellule"""
        if 0 <= x < self.height and 0 <= y < self.width: #verifie coordonee dans limites de grille 
            self.grid[x][y] = state # met a jour l etat de la cellule

    def count_neighbors(self, x, y): 
        """Compter les voisins vivants"""
        count = 0
        for i in range(-1, 2): #parcourir les voisins
            for j in range(-1, 2): #parcourir les voisins
                if i == 0 and j == 0:  # Ignorer la cellule elle-même
                    continue
                new_x, new_y = x + i, y + j # calcule les coordonnees des voisins 
                if 0 <= new_x < self.height and 0 <= new_y < self.width: 
                    count += self.grid[new_x][new_y] #complet les voisins 
        return count 

    def next_generation(self):
        """Calculer la prochaine génération"""
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)] 
        for x in range(self.height): # parcourir la grille heutaure
            for y in range(self.width):# largeur 
                neighbors = self.count_neighbors(x, y) 
                if self.grid[x][y] == 1:  # Cellule vivante
                    if neighbors < 2 or neighbors > 3:
                        new_grid[x][y] = 0  # Meurt
                    else:
                        new_grid[x][y] = 1  # Survit
                else:  # Cellule morte
                    if neighbors == 3:
                        new_grid[x][y] = 1  # Naissance
        self.grid = new_grid

    def display(self): 
        """Afficher la grille"""
        os.system('cls' if os.name == 'nt' else 'clear')  # Effacer l'écran
        for row in self.grid:
            print(' '.join(['■' if cell else '□' for cell in row])) #affichege
        print() 

# Version avec bordures extensibles 
'''class GameOfLifeExpandable: 
    def __init__(self, max_size=10000): 
        self.max_size = max_size 
        self.grid = {}  # Grille sparse avec coordonnées (x, y) pour cellules vivantes

    def set_cell(self, x, y, state):
        """Définir une cellule (1 = vivante, 0 = morte)"""
        if -self.max_size <= x <= self.max_size and -self.max_size <= y <= self.max_size: # limites de grille
            if state == 1: 
                self.grid[(x, y)] = 1 
            elif (x, y) in self.grid: 
                del self.grid[(x, y)]  # Supprimer si morte

    def count_neighbors(self, x, y):
        """Compter les voisins vivants"""
        count = 0
        for i in range(-1, 2): 
            for j in range(-1, 2): 
                if i == 0 and j == 0: 
                    continue
                count += (x + i, y + j) in self.grid
        return count

    def next_generation(self):
        """Calculer la prochaine génération"""
        new_grid = {}
        to_check = set()
        # Ajouter toutes les cellules vivantes et leurs voisins à vérifier
        for x, y in self.grid:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    to_check.add((x + i, y + j))

        # Appliquer les règles du jeu
        for x, y in to_check:
            neighbors = self.count_neighbors(x, y)
            if (x, y) in self.grid:  # Cellule vivante
                if 2 <= neighbors <= 3:
                    new_grid[(x, y)] = 1
            else:  # Cellule morte
                if neighbors == 3:
                    new_grid[(x, y)] = 1
        self.grid = new_grid

    def display(self, min_x=-5, max_x=5, min_y=-5, max_y=5):
        """Afficher une portion de la grille"""
        os.system('cls' if os.name == 'nt' else 'clear')
        for x in range(min_x, max_x + 1):
            row = []
            for y in range(min_y, max_y + 1):
                row.append('■' if (x, y) in self.grid else '□')
            print(' '.join(row))
        print()'''

# Fonctions pour exécuter les jeux
root = tk.Tk()
root.mainloop()
def run_fixed_game(initial_state, width=10, height=10, generations=10): 
    """Exécuter le jeu avec bordures fixes"""
    game = GameOfLifeFixed(width, height) #initialise
    for x, y in initial_state: #initialise cellules
        game.set_cell(x, y, 1) #cellule vivante
    
    print("Simulation avec bordures fixes :")
    for _ in range(generations): 
        game.display()  #affiche
        game.next_generation() 
        time.sleep(0.2) #pause

'''def run_expandable_game(initial_state, generations=10):
    """Exécuter le jeu avec bordures extensibles"""
    game = GameOfLifeExpandable()
    for x, y in initial_state:
        game.set_cell(x, y, 1)
    
    print("Simulation avec bordures extensibles :")
    for _ in range(generations):
        game.display(-5, 5, -5, 5)  # Fenêtre d'affichage
        game.next_generation()
        time.sleep(0.5)'''

# Configurations initiales
glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]  # Planeur
blinker = [(2, 1), (2, 2), (2, 3)]  # Clignotant
block = [(2, 2), (2, 3), (3, 2), (3, 3)]  # Bloc

# Exécuter les simulations
if __name__ == "__main__": 
    # Tester avec bordures fixes
    print("Planeur (Glider) - Bordures fixes :")
    run_fixed_game(glider)
    time.sleep(1)

    print("Clignotant (Blinker) - Bordures fixes :")
    run_fixed_game(blinker)
    time.sleep(1)

    print("Bloc (Block) - Bordures fixes :")
    run_fixed_game(block)
    time.sleep(1)
'''
# Tester avec bordures extensibles 
    print("Planeur (Glider) - Bordures extensibles :")
    run_expandable_game(glider)
    time.sleep(1)

    print("Clignotant (Blinker) - Bordures extensibles :")
    run_expandable_game(blinker)
    time.sleep(1)

    print("Bloc (Block) - Bordures extensibles :")
    run_expandable_game(block) '''