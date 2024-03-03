from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move


class Pawn(ChessPiece):
    """
    Pawn class as a child of ChessPiece
    """
    def __init__(self, Player):
        """
        Initialize class as a child of ChessPiece using super() method
        :param Player: team color of piece
        """
        super().__init__(Player)

    def __str__(self):
        """
        Returns team color of piece
        :return: player team color
        """
        return f'player is {self.player}'

    def type(self):
        """
        Returns type of piece
        :return: Pawn
        """
        return 'Pawn'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        """
        Determines whether the move is valid according to the move-set of the pawn
        :param move: move class containing start and end locations
        :param board: list of lists that creates a chessboard
        :return: true or false
        """
        if ChessPiece.is_valid_move(self, move, board):     # Check default move-set according to ChessPiece
            xdist = abs(move.to_col - move.from_col)    # Absolute value of x distance
            if xdist > 1:   # Cannot move horizontally
                return False
            ydist = (move.to_row - move.from_row)   # Direction and distance of the Pawn

            if self.player.name == 'BLACK':     # If pawn is on the black team
                if xdist == 1 and ydist != 1:   # Check if diagonal
                    return False
                if xdist == 1:      # If moving horizontally check whether attacking
                    if board[move.to_row][move.to_col] == None:
                        return False
                    elif board[move.to_row][move.to_col].player.name is self.player.name:
                        return False
                elif board[move.to_row][move.to_col] != None:
                        return False
                if ydist < 0:
                    return False
                if move.from_row == 1:      # If on initial pawn, can move twice but not over another piece
                    if ydist > 2:
                        return False
                    elif ydist == 2:
                        if board[move.to_row-1][move.to_col] is not None:
                            return False
                elif ydist > 1:
                        return False

            if self.player.name == 'WHITE': # Check whether on the white team, repeat checks above but in other direction
                if xdist == 1 and ydist != -1:
                    return False
                if xdist == 1:
                    if board[move.to_row][move.to_col] == None:
                        return False
                    elif board[move.to_row][move.to_col].player.name is self.player.name:
                        return False
                elif board[move.to_row][move.to_col] != None:
                        return False
                if ydist > 0:
                    return False
                if move.from_row == 6:
                    if ydist < -2:
                        return False
                    elif ydist == -2:
                        if board[move.to_row+1][move.to_col] is not None:
                            return False
                elif ydist < -1:
                        return False
            return True
        else:
            return False




