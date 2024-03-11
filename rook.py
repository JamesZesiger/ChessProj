"""
This modules purpose is to create the chess game functions
Author: James Zesiger, Quentin Daniere, Evan Bower
Date: 3/11/2024
Version: 1
"""
from typing import List
from chess_piece import ChessPiece
from move import Move


class Rook(ChessPiece):
    """
    The Rook class is a child of the ChessPiece class
    """
    def __init__(self, Player):
        """
        Initialize as a child of the ChessPiece class using super() method

        Parameters:
             Player: team color of piece
        """
        super().__init__(Player)

    def __str__(self):
        """
        Print the team color of the piece

        Returns: player color
        """
        return f'player is {self.player}'

    def type(self):
        """
        Return the type of piece

        Returns: Rook
        """
        return f'Rook'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        """
        Check whether the move is valid, specified for a Rook's moveset
        Parameters
            move: move class with start and end locations
            board: list of lists depicting a board

        Returns: True or False
        """
        if ChessPiece.is_valid_move(self,move,board):   # Check for default move validity from ChessPiece
            xdist = abs(move.to_col - move.from_col)    # absolute value of x distance
            ydist = abs(move.to_row - move.from_row)    # absolute value of y distance
            if (move.to_col - move.from_col != 0) and (move.to_row - move.from_row == 0):
                # Check whether Moving Horizontally
                if xdist == 1:  # If moving only 1 square
                    if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player.name is not self.player.name:
                        return True
                    else:
                        return False
                if move.to_col - move.from_col > 0:     # If vertically check all cases between start and end location
                    for i in range(move.from_col+1,move.to_col):
                        if board[move.from_row][i] is not None:
                            return False
                    return True
                else:
                    for i in range(move.to_col+1,move.from_col):
                        if board[move.from_row][i] is not None:
                            return False
                    return True
            elif (move.to_col - move.from_col == 0) and (move.to_row - move.from_row != 0):
                # If moving horizontally, check all cases between start and end locations unless moving one space
                if ydist == 1:
                    if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player.name is not self.player.name:
                        return True
                    else:
                        return False
                if abs(move.to_row - move.from_row) > 0:
                    if move.to_row > move.from_row:
                        for i in range(move.from_row+1,move.to_row):
                            if board[i][move.from_col] is not None:
                                return False
                    else:
                        for i in range(move.to_row+1,move.from_row):
                            if board[i][move.from_col] is not None:
                                return False
                    return True
                else:
                    for i in range(move.from_row-1,move.to_row+1):
                        if board[i][move.from_col] is not None:
                            return False
                    return True
            else:
                # Not moving Vertically or Horizontally so not allowed for a rook
                return False
