"""
This modules purpose is to create queen piece
Author: James Zesiger, Quentin Daniere, Evan Bower
Date: 3/11/2024
Version: 1
"""
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
        Parameters:
             Player: player color of piece
        """
        super().__init__(Player)

    def __str__(self):
        """
        Returns the team color of the piece
        Returns: player color
        """
        return f'player is {self.player}'

    def type(self):
        """
        Returns the type of piece
        Return: Queen
        """
        return f'Queen'

    def is_valid_move(self, move: Move, board) -> bool:
        """
        Since the queen moves like a bishop or a rook, if either of their moves are valid, the queen can move as well
        Parameters:
            move: move class containing start location and end location
            board: list of lists that creates the chessboard
        Return: true or false
        """
        if ChessPiece.is_valid_move(self, move, board):     # Check for default move validity
            if Rook.is_valid_move(self, move, board) or Bishop.is_valid_move(self, move, board):
                # If either the rook move or bishop move is valid, return true
                return True
        else:
            return False
