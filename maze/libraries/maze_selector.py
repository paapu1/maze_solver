import os

class MazeSelector():

    def __init__(self):
        self.startpoint = []
        self.maze_path = os.curdir + '/resources/'

    def get_maps_from_resources(self):
        """
        Tries to read and get map selection from resources folder
        """
        try:
            maze_selection = os.listdir(self.maze_path)
        except:
            print('Error: No mazes available at the moment')
            print('Hint: Add mazes to "resources" folder and try again')
        return maze_selection
    
    def show_maps_to_choose(self, maze_selection):
        """
        Prints mazes that are available to be selected for user
        

        Parameters
        maze_selection : list of str
        ----------
        """
        print('Step1: Select maze to solve, Step2: Follow solving process\n')
        print('Current selection of mazes:\n')
        for idx, maze_name in enumerate(maze_selection, start=1):
            print(f'{idx}: {maze_name}')
        print('\nType maze name in following format "maze_name.txt"')

    def maze_selector(self, maze_selection):
        """
        Maze selector

        Waiting for user given input which is assigned to: ``user_input``.
        User should give correct maze name or id of the map.

        User can also type "e" and enter to exit the program

        Looping until correct input is given

        Parameters
        ----------
        maze_selection : list of str
        """

        while(True):
            user_input_maze = input()

            if user_input_maze in maze_selection:
                print(f'Selected maze: {user_input_maze} to be solved.')
                return user_input_maze
            elif user_input_maze == 'e':
                exit()
            elif user_input_maze == 'm':
                self.show_maps_to_choose(maze_selection)
            else:
                print('Type correct maze name or "e" + press Enter to exit')
                print('Type "m" + press Enter to see maze selection again')

    def read_maze_file_to_matrix(self, selected_maze):
        """
        Reads user selected maze file to matrix array.


        """
        maze_as_matrix = []
        maze_path = os.curdir + '/resources/'
        try:
            with open(maze_path + selected_maze, 'r') as file:
                for row_index, row in enumerate(file):
                    chars_in_row = []
                    for char_index, char in enumerate(row):
                        chars_in_row.append(char)
                        if char == '^':
                            self.startpoint.append(row_index)
                            self.startpoint.append(char_index)
                    maze_as_matrix.append(chars_in_row[ : -1])
        except Exception:
            print("Encountered error while reading the maze file.")
            print("Closing maze solver.")
            exit()
        return maze_as_matrix

    def get_starting_point(self):
        """
        Get starting point for maze solver.
        """
        return self.startpoint

    def run_maze_selector(self):
        maze_selection = self.get_maps_from_resources()
        self.show_maps_to_choose(maze_selection)
        selected_maze = self.maze_selector(maze_selection)
        return selected_maze