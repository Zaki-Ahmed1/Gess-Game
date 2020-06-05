# Name: Zaki Ahmed
# Date: 28 May 2020
# Assignment: Portfolio Project

# Description: A game that is modeled off the Gess Game described in the README file.


# Define game class
class GessGame:
    """
    Parameters: n/a
    Methods/Returns: Req'd - Game State, Resign, Make Move  +  Additional - Display, Is Valid, Direction, Position, Distance
    Summary: A representation of the board as a 2D list object.
    """
    def __init__(self):
        """
        Parameters: n/a
        Data Members: Board (2D layout), Current Player, Game State
        Summary: Setup a standard board with the pieces in their default starting position. Black moves first. The following
                 methods are used to move and modify the board, current player, and game state.
        """
        # Build a board rows: 1->20 x columns: A->T, Black starts first, Game Unfinished until no ring is left (or resigns)
        self.current_player = 'B'
        self.game_status = 'UNFINISHED'
        self.board = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' '],
            [' ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' '],
            [' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
            [' ', 'B', 'B', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', ' '],
            [' ', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def get_game_state(self):
        """Returns status of the game"""
        return self.game_status

    def get_board(self):
        """Returns a 2D display of the board"""
        for i in range(20):
            for j in range(20):
                print(self.board[i][j], end='|')
            print()

    def resign_game(self):
        """Trigger an end of the game if a player doesn't wish to continue"""
        # If entered, it will return winner status for the opposing player
        if self.current_player == 'W':
            self.game_status = 'BLACK_WON'
        if self.current_player == 'B':
            self.game_status = 'WHITE_WON'

    def position_to_index(self, position):
        """
        Parameters: Position
        Returns: Row, Column
        Summary: Converts alphanumeric positions into index usable values for use in other functions
        """
        row = 20 - int(position[1:])
        col = ord(position[0]) - ord('a')
        return row, col

    def get_desired_direction(self, current_row, current_col, desired_row, desired_col):
        """
        Parameters: Current Row, Current Column, Desired Row, Desired Column
        Returns: Tuple of (Row, Column)
        Summary: Helps validate if the direction that the player requested is valid.
        """
        # UP DOWN LEFT RIGHT
        # East
        if desired_row == current_row and desired_col > current_col:
            return (0, 1)
        # West
        if desired_row == current_row and desired_col < current_col:
            return (0, -1)
        # North
        if desired_col == current_col and desired_row < current_row:
            return (-1, 0)
        # South
        if desired_col == current_col and desired_row > current_row:
            return (1, 0)

        # DIAGONALS
        # NorthEast
        if desired_row < current_row and desired_col > current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return (-1, 1)
        # NorthWest
        if desired_row < current_row and desired_col < current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return (-1, -1)
        # SouthEast
        if desired_row > current_row and desired_col > current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return (1, 1)
        # SouthWest
        if desired_row > current_row and desired_col < current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return (1, -1)
        return (0, 0)

    def get_distance_moved(self, current_row, current_col, desired_row, desired_col):
        """
        Parameters: Current Row, Current Column, Desired Row, Desired Column
        Returns: Distance of requested move
        Summary: Calculates if the distance of move and used in other functions to determine if number of moves is within limits.
        """
        return max(abs(current_row - desired_row), abs(current_col - desired_col))

    def is_valid(self, current_row, current_col, desired_row, desired_col):
        """
        Parameters: Current Row, Current Column, Desired Row, Desired Column
        Returns: Distance of requested move
        Summary: Calculates if the distance of move and used in other functions to determine if number of moves is within limits.
        """
        # If move is illegal, return False. Otherwise return False.

        # If the game is over, return False.
        if self.game_status != 'UNFINISHED':
            return False

        # Boundary Check to see if move is within the valid playing area (18x18)
        if (current_row < 1 or current_row > 18) or \
                (current_col < 1 or current_col > 18) or \
                (desired_row < 1 or desired_row > 18) or \
                (desired_col < 1 or desired_col > 18):
            return False

        # If the center is empty and distance moved is more than 3
        # return 3
        if self.board[current_row][current_col] == ' ' and self.get_distance_moved(current_row, current_col, desired_row, desired_col) > 3:
            return False

        # Define the opposite color
        opposite_color = ' '
        if self.current_player == 'B':
            opposite_color = 'W'
        if self.current_player == 'W':
            opposite_color = 'B'

        # Check if any stones of opposing color
        for row in range(-1, 2):
            for col in range(-1, 2):
                if self.board[current_row + row][current_col + col] == opposite_color:
                    return False

        # Check for stone along the direction moved
        (step_row, step_col) = self.get_desired_direction(current_row, current_col, desired_row, desired_col)

        # Invalid direction
        if (step_row, step_col) == (0, 0):
            return False

        if self.board[current_row + step_row][current_col + step_col] == ' ':
            return False

        # Check for Obstruction
        if self.is_move_obstructed(current_row, current_col, desired_row, desired_col):
            return False

        return True

    def has_stone_at(self, row, col):
        """
        Parameters: Row, Column
        Returns: Boolean
        Summary: Determines if a stone exists as passed in coordinates.
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.board[row + i][col + j] != ' ':
                    return True
        return False

    def remove_piece_at(self, row, col):
        """
        Parameters: Row, Column
        Returns: Game Piece
        Summary: Determines if a stone exists as passed in coordinates.
        """
        temp_piece = [[' '] * 3 for i in range(3)]
        for i in range(-1, 2):
            for j in range(-1, 2):
                temp_piece[i + 1][j + 1] = self.board[row + i][col + j]
                self.board[row + i][col + j] = ' '
        return temp_piece

    def place_piece_at(self, row, col, new_piece):
        """
        Parameters: Row, Column, Piece
        Returns: n/a
        Summary: Creates a new piece to place in proper position.
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                self.board[row + i][col + j] = new_piece[i + 1][j + 1]

    def is_move_obstructed(self, current_row, current_col, desired_row, desired_col):
        """
        Parameters: Current Row, Current Column, Desired Row, Desired Column
        Returns: Boolean
        Summary: Determines if a move is valid and unobstructed.
        """
        row_change, col_change = self.get_desired_direction(current_row, current_col, desired_row, desired_col)

        temp_piece = self.remove_piece_at(current_row, current_col)

        while current_row != desired_row and current_col != desired_col:
            if self.has_stone_at(current_row, current_col):
                self.place_piece_at(current_row, current_col, temp_piece)
                return True

            # Update the center direction
            current_row += row_change
            current_col += col_change

        self.place_piece_at(current_row, current_col, temp_piece)
        return False

    def move_piece(self, current_row, current_col, desired_row, desired_col):
        """
        Parameters: Current Row, Current Column, Desired Row, Desired Column
        Returns: n/a
        Summary: Moves the piece to the proper location and passes it into the helper function.
        """
        temp_piece = self.remove_piece_at(current_row, current_col)
        self.place_piece_at(desired_row, desired_col, temp_piece)

    def make_move(self, current, desired):
        """Take in the current attribute for the game piece, and where the player wants to move"""

        # Get the corresponding row and column indexes
        # for the given positions
        current_row, current_col = self.position_to_index(current)
        desired_row, desired_col = self.position_to_index(desired)

        board_copy = self.copy_board()

        # If it is valid
        if self.is_valid(current_row, current_col, desired_row, desired_col) == False:
            return False

        self.move_piece(current_row, current_col, desired_row, desired_col)

        if not self.has_ring(self.current_player):
            self.reset_board(board_copy)
            return False

        white_status = self.has_ring('W')
        black_status = self.has_ring('B')

        if white_status == True and black_status == True:
            self.game_status = 'UNFINISHED'

        if white_status != True and black_status == True:
            self.game_status = 'BLACK_WON'

        if white_status == True and black_status != True:
            self.game_status = 'WHITE_WON'

        # Update the player
        if self.current_player == 'W':
            self.current_player = 'B'
        else:
            self.current_player = 'W'

        self.get_board()
        print("")

        return True

    def copy_board(self):
        board_copy = [[' '] * 20 for _ in range(20)]
        for i in range(20):
            for j in range(20):
                board_copy[i][j] = self.board[i][j]

    def reset_board(self, board_copy):
        board_copy = [' ' * 20 for _ in range(20)]
        for i in range(20):
            for j in range(20):
                self.board[i][j] = board_copy[i][j]

    def has_ring(self, color):
        for i in range(2, 19):
            for j in range(2, 19):
                if self.board[i - 1][j] == color and \
                        self.board[i - 1][j + 1] == color and \
                        self.board[i][j + 1] == color and \
                        self.board[i + 1][j + 1] == color and \
                        self.board[i + 1][j] == color and \
                        self.board[i + 1][j - 1] == color and \
                        self.board[i][j - 1] == color and \
                        self.board[i - 1][j - 1] == color and \
                        self.board[i][j] == ' ':
                    return True
        return False


# For testing purposes only...
game = GessGame()
game.get_board()
print("--------------------------------------------")
print(game.make_move('c6', 'c7'))
print("--------------------------------------------")
print(game.make_move('c15', 'c14'))
print("--------------------------------------------")
print(game.make_move('c3','c5'))
print("--------------------------------------------")
print(game.make_move('c14', 'c13'))
print("--------------------------------------------")
print(game.make_move('c5','d5'))




# game.display_board()
