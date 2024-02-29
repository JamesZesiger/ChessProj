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
                # checks if anything is in the path
                distance = xdist
                xdist = move.to_col - move.from_col
                ydist = move.to_row - move.from_row
                if xdist > 0 and ydist > 0:  # Down and to the right
                    for i in range(1, distance):
                        if board[move.from_row+i][move.from_col+i] is not None:
                            return False
                    return True
                elif xdist > 0 > ydist:  # Up and to the right
                    for i in range(1, distance):
                        if board[move.from_row - i][move.from_col + i] is not None:
                            return False
                    return True
                elif xdist < 0 < ydist:  # Down and to the left
                    for i in range(1, distance):
                        if board[move.from_row + i][move.from_col - i] is not None:
                            return False
                    return True
                else:                           # Up and to the left
                    for i in range(1, distance):
                        if board[move.from_row - i][move.from_col - i] is not None:
                            return False
                    return True
            else:
                return False
        else:
            return False



