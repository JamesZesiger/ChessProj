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
        return (f'Team: {self.player.name}\n'
                f'Piece:King')

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
# test
class x(Enum):
    WHITE = 0
    BLACK = 1
w = King(x.WHITE)
b = King(x.BLACK)
m = Move(2,3,2,2)
m2 = Move(3,6,3,7)
board = [[None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,b   ,w   ,None,None,None,None],
        [None,None,None,w   ,None,None,None,None],
        [None,None,None,None,None,None,None,None]]
print(w.is_valid_move(m,board))
print(b.is_valid_move(m2,board))
print(w.player.name, w.player.value)
print(w.type())

