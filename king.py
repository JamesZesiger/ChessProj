"""
This modules purpose is to create the king piece
Author: James Zesiger, Quentin Daniere, Evan Bower
Date: 3/11/2024
Version: 1
"""
from typing import List
from chess_piece import ChessPiece
from move import Move


class King(ChessPiece):
    """
    Initialize the King class as a chesspiece using the super() method
    """
    def __init__(self, Player):
        """
        constructor for king piece
        Parameter:
            Player: player ownership of piece
        """
        super().__init__(Player)



    def __str__(self):
        """
        What team the piece belongs to

        Returns: f'player is {self.player}'
        """
        return f'player is {self.player}'

    def type(self):
        """
        the type of piece it is

        Returns: 'King'
        """
        return 'King'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        """
        A modified version of the is_valid_move method of the chess_piece class parent. It calls that method for general
        checks before checking for King specific movement validity.
        Parameters:
            move: input from move class, denoting start and end location
            board: the current board in play with all the pieces
        Returns: bool
        """
        if ChessPiece.is_valid_move(self, move, board):
            # Check overall validity from chess_piece class
            xdist = abs(move.to_col - move.from_col)    # absolute value of x distance
            ydist = abs(move.to_row - move.from_row)    # Absolute value of y distance
            if xdist < 2 and ydist < 2:
                # Check that distance is only 1 square away in all directions
                if board[move.to_row][move.to_col] is not None:
                    # if board sint an empty space
                    if board[move.to_row][move.to_col].player.name is not self.player.name:
                        # CHeck whether it's not same team
                        return True
                else:
                    return True
            return False

