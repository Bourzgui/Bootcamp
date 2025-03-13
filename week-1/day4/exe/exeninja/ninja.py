import random
import time

class GameOfLife:
    def __init__(self, rows, cols):
        
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
    def initialize_grid(self, initial_state=None):
        """ Initialiser la grille avec un état initial donné (ou aléatoire si None) """
        if initial_state:
            for (r, c) in initial_state:
                self.grid[r][c] = 1  
        else:
            
            for r in range(self.rows):
                for c in range(self.cols):
                    self.grid[r][c] = random.choice([0, 1])   
    
    def get_neighbours(self, row, col):
        """ Retourne les voisins d'une cellule donnée """
        neighbours = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]
        
        live_neighbours = 0
        for dr, dc in neighbours:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                live_neighbours += self.grid[r][c]
        
        return live_neighbours
    
    def apply_rules(self):
        """ Applique les règles du jeu à chaque cellule """
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbours = self.get_neighbours(r, c)
                
                if self.grid[r][c] == 1:   
                    if live_neighbours < 2 or live_neighbours > 3:
                        new_grid[r][c] = 0  
                    else:
                        new_grid[r][c] = 1   
                elif self.grid[r][c] == 0 and live_neighbours == 3:
                    new_grid[r][c] = 1  
                
        self.grid = new_grid
    
    def display_grid(self):
        """ Affiche la grille dans la console """
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print("\n" + "="*30 + "\n")
    
    def next_generation(self):
        """ Calcule la prochaine génération """
        self.apply_rules()
        self.display_grid()
    
 
game = GameOfLife(10, 10)

initial_state = [(3, 4), (3, 5), (3, 6), (2, 6), (1, 5)]
game.initialize_grid(initial_state)

game.display_grid()

 
for _ in range(10):
    time.sleep(1)  
    game.next_generation()
