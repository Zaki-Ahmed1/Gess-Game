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


    def display_board(self):
        for i in range(20):
            for j in range(20):
                print(self.board[i][j], end='|')
            print()

    def get_game_state(self):
        """Define the status of the game"""
        # If game is still active (i.e. Black or White >=1), return 'UNFINISHED'
        # If there are 0 white pieces, return 'BLACK_WON'
        # If there are 0 black pieces, return 'WHITE_WON'
        return self.game_status

    def resign_game(self):
        """Trigger an end of the game if a player doesn't wish to continue"""
        # If entered, it will return winner status for the opposing player
        if self.current_player == 'W':
            self.game_status = 'BLACK_WON'
        if self.current_player == 'B':
            self.game_status = 'WHITE_WON'

    def position_to_index(self, position):
        # c7, d14
        row = 20 - int(position[1:])
        col = ord(position[0]) - ord('a')
        return row, col

    def get_desired_direction(self, current_row, current_col, desired_row, desired_col):

        # UP DOWN LEFT RIGHT
        # East
        if desired_row == current_row and desired_col > current_col:
            return 'East'

        # West
        if desired_row == current_row and desired_col < current_col:
            return 'West'
        # North
        if desired_col == current_col and desired_row < current_row:
            return 'North'

        # South
        if desired_col == current_col and desired_row > current_row:
            return 'South'

        # DIAGONALS
        # NorthEast
        if desired_row < current_row and desired_col > current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return 'NorthEast'

        # NorthWest
        if desired_row < current_row and desired_col < current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return 'NorthEast'

        # SouthEast
        if desired_row > current_row and desired_col > current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return 'SouthEast'

        # SouthWest
        if desired_row > current_row and desired_col < current_col and \
                (abs(desired_row - current_row) == abs(desired_col - current_col)):
            return 'SouthWest'

        return "NA"

    def get_distance_moved(self, current_row, current_col, desired_row, desired_col):
        return max(abs(current_row - desired_row), abs(current_col - desired_col))

    def is_valid(self, current_row, current_col, desired_row, desired_col):
        """Will see if the move is within the confines of the board, then see if the move can be made"""
        # If valid return True, else return False

        # If the game is over, return false
        if self.game_status != 'UNFINISHED':
            return False

        # Boundary Check to see if move is within the valid playing area (18x18)
        if (current_row < 1 or current_row > 18) or \
                (current_col < 1 or current_col > 18) or \
                (desired_row < 1 or desired_row > 18) or \
                (desired_col < 1 or desired_col > 18):
            return False

        # if the center is empty and distance moved is more than 3
        # return 3
        if self.board[current_row][current_col] == ' ' and self.get_distance_moved(current_row, current_col,
                                                                                   desired_row,
                                                                                   desired_col) > 3:
            return False

        # Define the opposite color
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
        direction_moved = self.get_desired_direction(current_row, current_col, desired_row, desired_col)
        print('direction_moved =', direction_moved)

        # Invalid direction
        if direction_moved == "NA":
            return False

        # See if stone in the East
        if direction_moved == "East" and self.board[current_row][current_col + 1] == ' ':
            return False

        # See if stone in the West
        if direction_moved == "West" and self.board[current_row][current_col - 1] == ' ':
            return False

        # See if stone in the North
        if direction_moved == "North" and self.board[current_row - 1][current_col] == ' ':
            return False

        # See if stone in the South
        if direction_moved == "South" and self.board[current_row + 1][current_col] == ' ':
            return False

        # See if stone in the NorthEast
        if direction_moved == "NorthEast" and self.board[current_row - 1][current_col + 1] == ' ':
            return False

        # See if stone in the NorthWest
        if direction_moved == "NorthWest" and self.board[current_row - 1][current_col - 1] == ' ':
            return False

        # See if stone in the SouthEast
        if direction_moved == "SouthEast" and self.board[current_row + 1][current_col + 1] == ' ':
            return False

        # See if stone in the SouthWest
        if direction_moved == "SouthWest" and self.board[current_row + 1][current_col - 1] == ' ':
            return False

        # Check for Obstruction
        if self.is_move_obstructed(current_row, current_col, desired_row, desired_col):
            return False

        return True

    def has_stone_at(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.board[row + i][col + j] != ' ':
                    return True
        return False

    def remove_piece_at(self, row, col):
        temp_piece = [[' '] * 3 for i in range(3)]
        for i in range(-1, 2):
            for j in range(-1, 2):
                temp[i + 1][j + 1] = self.board[row + i][col + j]
                self.board[row + i][col + j] = ' '
        return temp_piece

    # def palce_piece_at(self, row, col, temp_piece):
    #     temp_piece = [[' '] * 3 for i in range(3)]
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
    #             self.board[row + i][col + j] = temp[i + 1][j + 1] =
    #             self.board[row + i][col + j] = ' '
    #     return temp_piece

    def is_move_obstructed(self, current_row, current_col, desired_row, desired_col):
        row_change, col_change = self.get_desired_direction(current_row, current_col, desired_row, desired_col)

        temp_piece = self.remove_piece_at(current_row, current_col)

        while current_row != desired_row and current_col != desired_col:
            if self.has_stone_at(current_row, current_col):
                return True

            # Update the center direction
            current_row += row_change
            current_col += col_change

        return False

    def make_move(self, current, desired):
        """Take in the current attribute for the game piece, and where the player wants to move"""

        # Get the corresponding row and column indexes
        # for the given positions
        current_row, current_col = self.position_to_index(current)
        desired_row, desired_col = self.position_to_index(desired)

        # If it is valid
        if self.is_valid(current_row, current_col, desired_row, desired_col) == False:
            return False

        # This will move any associated pieces that need to be moved too
        # It will remove the pieces that are captured, if any


game = GessGame()
game.display_board()
print(game.make_move('g2', 'e7'))