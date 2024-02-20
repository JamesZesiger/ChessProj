from chess_piece import ChessPiece
from move import Move

class Pawn(ChessPiece):
    def __init__(self, Player):
        super().__init__(Player)



    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return f'Pawn'


c = Pawn(1)
m = Move(1,1,2,2)
print(c.is_valid_move(m,[[Pawn,Pawn][Pawn,None]]))
c.player = 2
print(c.player)

