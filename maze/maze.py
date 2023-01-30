import os
import time
from libraries.maze_selector import MazeSelector
from libraries.maze_solver import MazeSolver

class Maze():

    maze_selector = MazeSelector()
    maze_solver = MazeSolver()

    def __init__(self):
        self.start_maze_solver()
        

    def welcome(self):
        """
        Print welcome text.
        """
        print('# # # # # # # # # # # # # #')
        print('# Welcome to maze solver  #')
        print('# # # # # # # # # # # # # #')

    def start_maze_solver(self):
        """
        Start maze solver.
        
        Print welcome, 
        Run maze selector for user, user can select maze to be solved.
        Solve maze. Solver will try solving maze three times each
        with different amount of moves (20, 50, 200).
        """

        self.welcome()
        selected_maze = self.maze_selector.run_maze_selector()
        self.maze_solver.solve_maze_three_times(selected_maze)

if __name__ == "__main__":
    Maze()