"""
This modules purpose is to create the bishop piece
Author: James Zesiger, Quentin Daniere, Evan Bower
Date: 3/11/2024
Version: 1
"""
from typing import List
from chess_piece import ChessPiece
from move import Move


class Bishop(ChessPiece):
    """
    Bishop class inherits from ChessPiece to create the bishop piece
    """
    def __init__(self, player):
        """
        constructor for Bishop class

        Parameters:
            player: Enum for piece color
        """
        super().__init__(player)

    def __str__(self):
        """
        string override that returns player name

        Returns: str
        """
        return f'Player is {self.player}'

    def type(self):
        """
        method that returns piece type

        Returns: str
        """
        return f'Bishop'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        """
        method that checks if move is valid for bishop

        Parameters:
            move: desired moves
            board: current board

        Returns: bool
        """
        if ChessPiece.is_valid_move(self, move, board):
            xdist = abs(move.to_col - move.from_col)
            ydist = abs(move.to_row - move.from_row)
            # checks to make sure movement is diagonal
            if xdist == ydist:
                # checks if anything is in the path
                distance = xdist
                xdist = move.to_col - move.from_col
                ydist = move.to_row - move.from_row
                if xdist > 0 and ydist > 0:  # Down and to the right
                    for i in range(1, distance):
                        if board[move.from_row+i][move.from_col+i] is not None:
                            return False
                    return True
                elif xdist > 0 > ydist:  # Up and to the right
                    for i in range(1, distance):
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
                    return True
                elif xdist < 0 < ydist:  # Down and to the left
                    for i in range(1, distance):
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
                    return True
                else:  # Up and to the left
                    for i in range(1, distance):
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
                    return True
            else:
                return False
        else:
            return False



