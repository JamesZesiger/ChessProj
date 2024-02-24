from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move


class Knight(ChessPiece):
    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return f'Knight'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        if ChessPiece.is_valid_move(self,move,board):
            xdist = abs(move.to_col - move.from_col)
            ydist = abs(move.to_row - move.from_row)
            if xdist + ydist == 3:
                if xdist > 2:
                    return False
                elif ydist > 2:
                    return False
            else:
                return False


'''
class x(Enum):
    WHITE = 0
    BLACK = 1
c = Knight(x.WHITE)
p = Knight(x.BLACK)
m = Move(0,1,2,3)
board = [[None,None,None,c,None,None,None,None],
        [None,None,None,None,p   ,None,None,None],
        [p,None,None,None,None,p,None,None],
        [None,None,None,None,None,None,p,None],
        [None,None,c,None,None,None,None,None],
        [None,None,None,c,None,None,None,None],
        [None,None,None,None,c   ,None,None,None],
        [None,None,None,None,None,None,None,None]]
print(c.is_valid_move(m,board))
'''
