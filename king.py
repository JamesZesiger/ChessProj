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
            ydist = abs(move.to_row - move.from_row)
            if xdist < 2 and ydist < 2:
                if board[move.to_row][move.to_col] is not None:
                    if board[move.to_row][move.to_col].player.name is not self.player.name:
                        return True
                else:
                    return True
            return False

