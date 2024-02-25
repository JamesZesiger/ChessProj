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
            r = Rook(self.player)
            b = Bishop(self.player)
            if r.is_valid_move(move, board) or b.is_valid_move(move, board):
                return True
            else:
                return False
        else:
            return False


class x(Enum):
    WHITE = 0
    BLACK = 1


q = Queen(x.WHITE)
p = Rook(x.BLACK)
m = Move(0,3,0,0)
board = [[None,None,None,q,None,None,None,None],
        [None,None,None,None,p   ,None,None,None],
        [p,None,None,None,None,p,None,None],
        [None,None,None,None,None,None,p,None],
        [None,None,q,None,None,None,None,None],
        [None,None,None,q,None,None,None,None],
        [None,None,None,None,q,None,None,None],
        [None,None,None,None,None,None,None,None]]
print(q.is_valid_move(m,board))


