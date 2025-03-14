import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.resizable(False, False)
root.title("Game of Life - Enhanced")

class GameOfLifeFixed:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.generation = 0
        self.live_cells = 0

    def set_cell(self, x, y, state):
        if 0 <= x < self.height and 0 <= y < self.width:
            self.grid[x][y] = state

    def count_neighbors(self, x, y): 
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_x, new_y = x + i, y + j
                if 0 <= new_x < self.height and 0 <= new_y < self.width:
                    count += self.grid[new_x][new_y]
        return count 

    def next_generation(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        live_count = 0
        for x in range(self.height):
            for y in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.grid[x][y] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[x][y] = 0
                    else:
                        new_grid[x][y] = 1
                        live_count += 1
                else:
                    if neighbors == 3:
                        new_grid[x][y] = 1
                        live_count += 1
        self.grid = new_grid
        self.generation += 1
        self.live_cells = live_count

# UI Setup
main_frame = tk.Frame(root, bg="#2b2b2b")
main_frame.pack(padx=25, pady=25)

# Split screen frames
left_frame = tk.Frame(main_frame, bg="#2b2b2b")
left_frame.grid(row=0, column=0, padx=5)
right_frame = tk.Frame(main_frame, bg="#2b2b2b")
right_frame.grid(row=0, column=1, padx=5)

# Canvas for game
canvas = tk.Canvas(left_frame, width=500, height=500, bg="#1e1e1e")
canvas.pack()

# Control panel
control_frame = tk.Frame(right_frame, bg="#2b2b2b")
control_frame.pack(pady=15)

# Variables
game = GameOfLifeFixed(15, 15)
running = False
CELL_SIZE = 50
cell_color = tk.StringVar(value="black")
dark_mode = tk.BooleanVar(value=True)

# Score display
score_label = tk.Label(control_frame, text="Generation: 0 | Live Cells: 0", 
                      fg="white", bg="#2b2b2b", font=("Arial", 12))
score_label.pack(pady=5)

def draw_grid():
    canvas.delete("all")
    for x in range(game.height):
        for y in range(game.width):
            x1 = y * CELL_SIZE
            y1 = x * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = cell_color.get() if game.grid[x][y] == 1 else "#ffffff" if not dark_mode.get() else "#1e1e1e"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def update_simulation():
    if running:
        game.next_generation()
        draw_grid()
        score_label.config(text=f"Generation: {game.generation} | Live Cells: {game.live_cells}")
        root.after(200, update_simulation)

def start_simulation():
    global running
    running = True
    glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    for x, y in glider:
        game.set_cell(x, y, 1)
    draw_grid()
    update_simulation()

def stop_simulation():
    global running
    running = False

def toggle_dark_mode():
    if dark_mode.get():
        root.configure(bg="#2b2b2b")
        main_frame.configure(bg="#2b2b2b")
        left_frame.configure(bg="#2b2b2b")
        right_frame.configure(bg="#2b2b2b")
        control_frame.configure(bg="#2b2b2b")
        canvas.configure(bg="#1e1e1e")
    else:
        root.configure(bg="#ffffff")
        main_frame.configure(bg="#ffffff")
        left_frame.configure(bg="#ffffff")
        right_frame.configure(bg="#ffffff")
        control_frame.configure(bg="#ffffff")
        canvas.configure(bg="#f0f0f0")
    draw_grid()

# Controls
tk.Button(control_frame, text="Start", command=start_simulation, bg="#404040", fg="white").pack(pady=5)
tk.Button(control_frame, text="Stop", command=stop_simulation, bg="#404040", fg="white").pack(pady=5)

# Color selection
color_frame = tk.LabelFrame(control_frame, text="Cell Color", bg="#2b2b2b", fg="white")
color_frame.pack(pady=5)
colors = [("Red", "#ff4444"), ("Green", "#44ff44"), ("Blue", "#4444ff"), ("Black", "black")]
for name, color in colors:
    tk.Radiobutton(color_frame, text=name, value=color, variable=cell_color, 
                  command=draw_grid, bg="#2b2b2b", fg="white", 
                  selectcolor="#404040").pack(anchor="w")

# Dark mode toggle
tk.Checkbutton(control_frame, text="Dark Mode", variable=dark_mode, 
              command=toggle_dark_mode, bg="#2b2b2b", fg="white",
              selectcolor="#404040").pack(pady=5)

# Initial setup
draw_grid()
toggle_dark_mode()

if __name__ == "__main__":
    root.mainloop()