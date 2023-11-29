import random
import tkinter as tk

grid_size = 10
num_of_ships = 5
max_guesses = 25

class BattleshipGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Battleship Game")
        self.geometry("800x800")
        self.configure(bg="yellow")

        self.grid_frame = tk.Frame(self, bg="yellow")
        self.grid_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.grid_buttons = [[None] * grid_size for _ in range(grid_size)]
        self.grid = [[""] * grid_size for _ in range(grid_size)]
        self.setup_board()
        self.create_grid_buttons()
        self.guesses = 0

    def setup_board(self):
        random_ships = 0
        for i in range(grid_size):
            for j in range(grid_size):
                self.grid[i][j] = "."

        while random_ships < num_of_ships:
            random_row = random.randint(0, grid_size - 1)
            random_col = random.randint(0, grid_size - 1)

            if self.grid[random_row][random_col] != "S":
                self.grid[random_row][random_col] = "S"
                random_ships += 1

    def create_grid_buttons(self):
        for i in range(grid_size):
            for j in range(grid_size):
                button = tk.Button(self.grid_frame, text="", width=8, height=4, command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                button.configure(bg="lightblue")
                self.grid_buttons[i][j] = button

    def draw_board(self):
        for i in range(grid_size):
            for j in range(grid_size):
                if self.grid[i][j] == " " or self.grid[i][j] == "S":
                    self.grid_buttons[i][j].config(text=".")
                else:
                    self.grid_buttons[i][j].config(text=self.grid[i][j])

    def button_click(self, row, col):
        if self.grid[row][col] == "S":
            print("Hit!")
            self.grid[row][col] = "X"
        else:
            print("Miss!")
            self.grid[row][col] = "O"

        self.guesses += 1
        if self.guesses >= max_guesses:
            print("Too many guesses! You lose. The correct answer was:")
            self.draw_board()
            self.destroy()
            return

        self.draw_board()
        if self.is_game_over():
            print("GAME OVER!")
            self.destroy()

    def is_game_over(self):
        for i in range(grid_size):
            for j in range(grid_size):
                if self.grid[i][j] == "S":
                    return False
        return True

if __name__ == "__main__":
    app = BattleshipGUI()
    app.mainloop()