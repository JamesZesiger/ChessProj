from enum import Enum

from chess_piece import ChessPiece
from move import Move
from bishop import Bishop
from rook import Rook


class Queen(ChessPiece):
    """
    Queen class created as a child of the ChessPiece class
    """
    def __init__(self, Player):
        """
        intialize queen piece using super() method
        :param Player: player color of piece
        """
        super().__init__(Player)

    def __str__(self):
        """
        Returns the team color of the piece
        :return: player color
        """
        return f'player is {self.player}'

    def type(self):
        """
        Returns the type of piece
        :return: Queen
        """
        return f'Queen'

    def is_valid_move(self, move: Move, board) -> bool:
        """
        Since the queen moves like a bishop or a rook, if either of their moves are valid, the queen can move as well
        :param move: move class containing start location and end location
        :param board: list of lists that creates the chessboard
        :return: true or false
        """
        if ChessPiece.is_valid_move(self, move, board):     # Check for default move validity
            if Rook.is_valid_move(self, move, board) or Bishop.is_valid_move(self, move, board):
                # If either the rook move or bishop move is valid, return true
                return True
        else:
            return False
