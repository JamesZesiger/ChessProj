from enum import Enum

from chess_piece import ChessPiece
from move import Move
from bishop import Bishop
from rook import Rook


class Queen(ChessPiece):
    def __init__(self, Player):
        super().__init__(Player)

    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return f'Queen'

    def is_valid_move(self, move: Move, board):
        if ChessPiece.is_valid_move(self, move, board):
            if Rook.is_valid_move(self, move, board) or Bishop.is_valid_move(self, move, board):
                return True
        else:
            return False



