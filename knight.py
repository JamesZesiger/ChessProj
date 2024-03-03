from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move


class Knight(ChessPiece):
    """
    The knight piece is a child of the ChessPiece class with a customized move set, specific to the knight.
    """
    def __init__(self, player):
        """
        initialize the piece using the super() method
        :param player: team color of piece
        """
        super().__init__(player)

    def __str__(self):
        """
        Returns the piece color of the initialized piece
        :return: player color
        """
        return f'player is {self.player}'

    def type(self):
        """
        Returns the type of piece, in this case knight
        :return: piece type
        """
        return f'Knight'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        """
        Determine the validity of the move for the piece
        :param move: move class containing start location and target location
        :param board: the board that the move will be played on
        :return: true or false
        """
        if ChessPiece.is_valid_move(self,move,board):   # Check whether basic move of ChessPiece is valid
            xdist = abs(move.to_col - move.from_col)    # Absolute value of the x distance
            ydist = abs(move.to_row - move.from_row)    # Absolute value of the y distance
            if xdist + ydist == 3:  # Total movement must equal 3
                if xdist > 2:   # Piece cannot move 3 on only x-axis
                    return False
                elif ydist > 2:     # Piece cannot move 3 on only y-axis
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False
