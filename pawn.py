from enum import Enum
from typing import List

from chess_piece import ChessPiece
from move import Move

class Pawn(ChessPiece):
    def __init__(self, Player):
        super().__init__(Player)



    def __str__(self):
        return f'player is {self.player}'

    def type(self):
        return 'Pawn'

    def is_valid_move(self, move: Move, board: List[List[ChessPiece]]):

        if ChessPiece.is_valid_move(self, move, board):
            xdist = abs(move.to_col - move.from_col)
            if xdist > 1:
                return False
            ydist = (move.to_row - move.from_row)

            if self.player.name == 'BLACK':
                if xdist == 1 and ydist != 1:
                    return False
                if xdist == 1:
                    if board[move.to_row][move.to_col] == None:
                        return False
                    elif board[move.to_row][move.to_col].player.name is self.player.name:
                        return False
                elif board[move.to_row][move.to_col] != None:
                        return False
                if ydist < 0:
                    return False
                if move.from_row == 1:
                    if ydist > 2:
                        return False
                elif ydist > 1:
                        return False

            if self.player.name == 'WHITE':
                if xdist == 1 and ydist != -1:
                    return False
                if xdist == 1:
                    if board[move.to_row][move.to_col] == None:
                        return False
                    elif board[move.to_row][move.to_col].player.name is self.player.name:
                        return False
                elif board[move.to_row][move.to_col] != None:
                        return False
                if ydist > 0:
                    return False
                if move.from_row == 6:
                    if ydist < -2:
                        return False
                elif ydist < -1:
                        return False
            return True
        else:
            return False




