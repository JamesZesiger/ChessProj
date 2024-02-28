from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move
from pawn import Pawn


class Rook(ChessPiece):
    def __init__(self, Player):
        super().__init__(Player)



    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return f'Rook'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):
        if ChessPiece.is_valid_move(self,move,board):
            xdist = abs(move.to_col - move.from_col)
            ydist = abs(move.to_row - move.from_row)
            if (move.to_col - move.from_col != 0) and (move.to_row - move.from_row == 0):
                # Moving Horizontally
                if xdist == 1:
                    if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player.name is not self.player.name:
                        return True
                    else:
                        return False
                if move.to_col - move.from_col > 0:
                    for i in range(move.from_col+1,move.to_col):
                        if board[move.from_row][i] is not None:
                            return False
                    return True
                else:
                    for i in range(move.to_col+1,move.from_col):
                        if board[move.from_row][i] is not None:
                            return False
                    return True
            elif (move.to_col - move.from_col == 0) and (move.to_row - move.from_row != 0):
                # Moving Vertically
                if ydist == 1:
                    if board[move.to_row][move.to_col] is None or board[move.to_row][move.to_col].player.name is not self.player.name:
                        return True
                    else:
                        return False
                if abs(move.to_row - move.from_row) > 0:
                    if self.player.name == 'WHITE':
                        for i in range(move.from_row+1,move.to_row):
                            if board[i][move.from_col] is not None:
                                return False
                    else:
                        for i in range(move.to_row+1,move.from_row):
                            if board[i][move.from_col] is not None:
                                return False
                    return True
                else:
                    for i in range(move.from_row-1,move.to_row+1):
                        if board[i][move.from_col] is not None:
                            return False
                    return True
            else:
                # Not moving Vertically or Horizontally
                return False

'''
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
'''
