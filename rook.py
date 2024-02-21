from chess_piece import ChessPiece
from move import Move


class Rook(ChessPiece):
    def __init__(self, Player):
        super().__init__(Player)



    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return f'Rook'

    def is_valid_move(self, move: Move, board) -> bool:
        if move.from_col == move.to_col and move.from_row == move.to_row:
            return False
        elif not 0 <= move.to_row <= 8 or 0 <= move.to_col <= 8:
            return False
        elif board[move.from_row][move.from_col] is None:
            return False
        elif board[move.to_row][move.to_col] is not self.__player.name:
            #In this function, check whether path in chosen direction is clear
            if (move.to_col - move.from_col != 0) and (move.to_row - move.from_row == 0):
                # Moving Vertically
                if move.to_col - move.from_col > 0:
                    for i in range(move.from_col,move.to_col-1):
                        if board[move.from_row][i] is not None:
                            return False
                    return True
                else:
                    for i in range(move.from_col,move.to_col+1):
                        if board[move.from_row][i] is not None:
                            return False
                    return True
            elif (move.to_col - move.from_col == 0) and (move.to_row - move.from_row != 0):
                # Moving Horizontally
                if move.to_row - move.from_row > 0:
                    for i in range(move.from_row,move.to_row-1):
                        if board[i][move.from_col] is not None:
                            return False
                    return True
                else:
                    for i in range(move.from_row,move.to_row+1):
                        if board[i][move.from_col] is not None:
                            return False
                    return True
            else:
                # Not moving Vertically or Horizontally
                return False
        else:
            return True


c = Rook(1)
m = Move(1,1,2,2)
print(c.is_valid_move(m,[[Rook,Rook][Rook,None]]))
c.player = 2
print(c.player)

