from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move


class Bishop(ChessPiece):

    def __init__(self, player):
        super().__init__(player)

    def __str__(self):
        return f'PLayer is {self.player}'

    def type(self):
        return f'Bishop'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        if ChessPiece.is_valid_move(self, move, board):
            xdist = abs(move.to_col - move.from_col)
            ydist = abs(move.to_row - move.from_row)
            # checks to make sure movement is diagonal
            if xdist == ydist:
                # checks if anything is in the path, currently doesn't work
                for i in range(move.from_col + 1, move.to_col - 1):
                    if board[move.from_row][i] is not None:
                        return False
                for i in range(move.from_row - 1, move.to_row + 1):
                    if board[move.from_col][i] is not None:
                        return False
                return True
            else:
                return False
        else:
            return True


'''
class x(Enum):
        WHITE = 0
        BLACK = 1
    w = Bishop(x.WHITE)
    b = Bishop(x.BLACK)
    m = Move(0, 1, 2, 3)
    m2 = Move(0, 1, 2, 3)
    board = [[None,None,None,None,None,None,None,None],
        [None,None,None,None,w,None,None,None],
        [None,None,None,None,None,w,None,None],
        [None,None,None,None,None,None,b,None],
        [None,None,w,None,None,None,None,None],
        [None,None,None,b,None,None,None,None],
        [None,None,None,None,b,None,None,None],
        [None,None,None,None,None,None,None,None]]
    print(w.is_valid_move(m, board))
    print(b.is_valid_move(m2, board))
    print(w.player.name, w.player.value)
'''
