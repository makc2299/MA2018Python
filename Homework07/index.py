"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

# Function that merges a single row or column in 2048.
def merge(line):
    result_list = [i for i in line if i != 0]
    while len(result_list) < len(line):
        result_list.append(0)
    for i in range(len(result_list) - 1):
        if result_list[i] == result_list[i + 1]:
            result_list[i] = 2 * result_list[i]
            result_list[i + 1] = 0
    # moves zeros to the end of the list
    while 0 in result_list:
        result_list.remove(0)
    while len(result_list) < len(line):
        result_list.append(0)
    return result_list

class TwentyFortyEight:
    # Class to run the game logic.

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.stop = False
        self.reset()

    def reset(self):
        self.grid = [[0 for i in range(self.width)] for j in range(self.height)]
        self.new_tile()
        
    def __str__(self):
        # Return a string representation of the grid for debugging.
        return str(self.grid)

    def get_grid_height(self):
        return self.height

    def get_grid_width(self):
        return self.width

    def move(self, direction):
        dir = OFFSETS[direction]
        temporary_grid = []        
        if direction == 1:
            for i in range(self.width):
                a = 0
                temporary_list = []
                for j in range(self.height):
                    temporary_list.append(self.grid[a][i])
                    a += dir[0]
                temporary_grid.append(merge(temporary_list))
            for i in range(self.height):
                for j in range(self.width):
                    self.grid[i][j] = temporary_grid[j][i]

        elif direction == 2:
            for i in range(self.width):
                a = self.height - 1
                temporary_list = []
                for j in range(self.height):
                    temporary_list.append(self.grid[a][i])
                    a += dir[0]
                temporary_grid.append(merge(temporary_list))
            for i in range(self.height):
                for j in range(self.width):
                    self.grid[i][j] = temporary_grid[j][self.height - 1 - i]
            
        elif direction == 3:
            for i in range(self.height):
                a = 0
                temporary_list = []
                for j in range(self.width):
                    temporary_list.append(self.grid[i][a])
                    a += dir[1]
                temporary_grid.append(merge(temporary_list))
            for i in range(self.height):
                for j in range(self.width):
                    self.grid[i][j] = temporary_grid[i][j]
         
        elif direction == 4:
            for i in range(self.height):
                a = self.width - 1
                temporary_list = []
                for j in range(self.width):
                    temporary_list.append(self.grid[i][a])
                    a += dir[1]
                temporary_grid.append(merge(temporary_list))
            for i in range(self.height):
                for j in range(self.width):
                    self.grid[i][j] = temporary_grid[i][self.width - 1 - j]
        f = 1
        for line in self.grid:
            for element in line:
                f *= element
                if f == 0:
                    self.stop = False
                    break
                else:
                    self.stop = True
        if not self.stop:
            self.new_tile()
            self.stop = False
    def new_tile(self):
        f = 0
        while f < 1:
            idx_i = random.randrange(self.height)
            idx_j = random.randrange(self.width)
            if self.grid[idx_i][idx_j] == 0:
                self.set_tile(idx_i, idx_j, random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4]))
                f += 1

    def set_tile(self, row, col, value):
        self.grid[row][col] = value

    def get_tile(self, row, col):
        # Return the value of the tile at position row, col.
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
