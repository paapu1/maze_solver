import os
import time
from libraries.maze_selector import MazeSelector

class MazeSolver():

    def __init__(self):
        self.maximum_moves = [20, 150, 200]
        self.number_of_moves = 0
        self.maze_file = ''
        self.max_moves = ''
        self.correct_path = []
        self.startpoint = []
        self.solution_path = os.curdir + '/solutions/'
        self.maze_selector = MazeSelector()

    def solve_maze_three_times(self, selected_maze):
        '''
        Trying to solve maze three times with different amount of moves.
        Using sleeps, so user can follow the process in terminal.
        '''
        time.sleep(4)
        for moves in self.maximum_moves:
            print(f'Trying to solve maze with: {moves} moves')
            time.sleep(4)
            self.max_moves = moves
            self.solve_maze(selected_maze)

    def solve_maze(self, selected_maze):
        '''
        Solving selected maze. 
        Reads selected maze text file to matrix, 
        so solve function can handle it.

        Starts solving algorithm and finally makes call to
        write the solution back to text file.

        Parameters
        ----------
        selected_maze : str
        '''
        self.maze_file = self.maze_selector.read_maze_file_to_matrix(selected_maze)
        self.correct_path = self.maze_selector.read_maze_file_to_matrix(selected_maze)
        starting_point = self.maze_selector.get_starting_point()
        solution_type = 'found'
        self.number_of_moves = 0

        if self.solve(starting_point[0], starting_point[1]):
            self.solution_found()
        else:
            solution_type = 'no'
            self.no_solution_found()

        time.sleep(4)
        self.write_solutions_to_file(selected_maze, solution_type)

    def write_solutions_to_file(self, selected_maze, solution_type):
        '''
        Writes solutions and no solutions to file.
        Prints path to solution files.

        Parameters
        ----------
        selected_maze : str
        solution_type : str
        '''
        solution_fname = selected_maze[:-4] + \
            f"-{self.max_moves}-moves-{solution_type}-solution.txt"

        with open(self.solution_path + solution_fname, 'w') as file:
                if solution_type == 'found':
                    file.write(self.maze_printer(self.correct_path))
                else:
                    file.write(self.maze_printer(self.maze_file))
        print(f"Solution saved to: {self.solution_path}{solution_fname}")

    def solution_found(self):
        '''
        Prints if solution was found.
        Solution can be found from correct_path.
        '''
        print('Found the exit, here is the correct path')
        print(self.maze_printer(self.correct_path))

    def no_solution_found(self):
        '''
        Prints if solution was not found.
        Partial solution is in the maze_file.
        '''
        print('There is no exit in the maze, this is the partial path')
        print(self.maze_printer(self.maze_file))

    def solve(self, x, y):
        '''
        Solve algorithm. Uses recursive search.
        Sleeping for tiny amount so user can follow solving process.

        Parameters
        ----------
        x : int
        y : int

        Returns:
        ------
        Boolean: True if exit is found, False if exit is not found
        '''
        
        time.sleep(0.01)
        print(f'Solving maze, move: {self.number_of_moves}')
        print(self.maze_printer(self.maze_file))
        
        if self.number_of_moves >= self.max_moves:
            return False
        if self.maze_file[x][y] == 'E':
            return True
        elif (self.maze_file[x][y] == '#' or self.maze_file[x][y] == '@'):
            return False

        self.maze_file[x][y] = '@'
        self.number_of_moves = self.number_of_moves + 1

        if (self.solve(x, y-1)
            or self.solve(x-1, y)
            or self.solve(x, y+1)
            or self.solve(x+1, y)):
            
            self.correct_path[x][y] = '.'
            return True

        return False

    def maze_printer(self, maze_matrix):
        '''
        Maze printer.
        Goes through maze matrix and prints it in more
        readable form.

        Parameters
        ----------
        maze_file : list of arraylists
        Example.
        '''
        return '\n'.join(''.join(map(str, row)) for row in maze_matrix)