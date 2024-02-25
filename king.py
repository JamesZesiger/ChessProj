from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move

class King(ChessPiece):
    def __init__(self, Player):
        super().__init__(Player)



    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return 'King'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        if ChessPiece.is_valid_move(self, move, board):
            xdist = abs(move.to_col - move.from_col)
            if xdist > 1:
                return False
            ydist = abs(move.to_row - move.from_row)
            if ydist > 1:
                return False
            else:
                return True

