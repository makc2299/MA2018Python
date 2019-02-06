"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.__init__(self, self.get_grid_height(), self.get_grid_width())
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie
            
    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
            
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        #poc_grid.Grid.__init__(self, self.get_grid_height(), self.get_grid_width())
        #visited = self._cells
        visited = [[EMPTY for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]
        distance_field = [[self.get_grid_height()*self.get_grid_width() for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]
        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for cell in self.humans():
                boundary.enqueue(cell)
        else:
            for cell in self.zombies():
                boundary.enqueue(cell)

        for cell in boundary:
            visited[cell[0]][cell[1]] = FULL
            distance_field[cell[0]][cell[1]] = 0
        
        while len(boundary)!= 0:
            current_cell = boundary.dequeue()
            neighbours = self.four_neighbors(current_cell[0],current_cell[1])
            for neigh in neighbours:
                if visited[neigh[0]][neigh[1]] == EMPTY and self.is_empty(neigh[0],neigh[1]):
                    visited[neigh[0]][neigh[1]] = FULL
                    boundary.enqueue(neigh)
                    distance_field[neigh[0]][neigh[1]]=distance_field[current_cell[0]][current_cell[1]] + 1


        return distance_field        

    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for index in range(len(self._human_list)):
            human = self._human_list[index]
            distance = zombie_distance_field[human[0]][human[1]]
            neighbors = self.eight_neighbors(human[0],human[1]) 
            pos = human
            best_dis = distance
            for neighbor in neighbors:
                if zombie_distance_field[neighbor[0]][neighbor[1]] > best_dis and self.is_empty(neighbor[0],neighbor[1]):
                    best_dis = zombie_distance_field[neighbor[0]][neighbor[1]]
                    pos = neighbor
            self._human_list[index] = pos
        
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for index in range(len(self._zombie_list)):
            zombie = self._zombie_list[index]
            distance = human_distance_field[zombie[0]][zombie[1]]
            neighbors = self.four_neighbors(zombie[0],zombie[1])
            pos = zombie
            best_dis = distance
            for neighbor in neighbors:
                if human_distance_field[neighbor[0]][neighbor[1]] < best_dis and self.is_empty(neighbor[0],neighbor[1]):
                    best_dis = human_distance_field[neighbor[0]][neighbor[1]]
                    pos = neighbor
            self._zombie_list[index] = pos

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
