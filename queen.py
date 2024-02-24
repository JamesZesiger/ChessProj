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

    def is_valid_move(self, move: Move, board) -> bool:
        if ChessPiece.is_valid_move(self, move, board):
            if Rook.is_valid_move(Rook, move, board) or Bishop.is_valid_move(Bishop, move, board):
                return True
        else:
            return False


"""
class x(Enum):
    WHITE = 0
    BLACK = 1
c = Rook(x.WHITE)
p = Pawn(x.BLACK)
m = Move(0,3,5,3)
board = [[None,None,None,c,None,None,None,None],
        [None,None,None,None,p   ,None,None,None],
        [p,None,None,None,None,p,None,None],
        [None,None,None,None,None,None,p,None],
        [None,None,c,None,None,None,None,None],
        [None,None,None,c,None,None,None,None],
        [None,None,None,None,c   ,None,None,None],
        [None,None,None,None,None,None,None,None]]
print(c.is_valid_move(m,board))
"""

