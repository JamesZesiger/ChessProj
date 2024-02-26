from copy import deepcopy
from enum import Enum
from typing import List

import move
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from move import Move

class MoveValidity(Enum):
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        if self.value == 2:
            return 'Invalid move.'

        if self.value == 3:
            return 'Invalid -- cannot move into check.'

        if self.value == 4:
            return 'Invalid -- must move out of check.'


# TODO: create UndoException
class UndoException(Exception):
    pass

class ChessModel:
    def __init__(self):
        wk = King(Player.WHITE)
        wp = Pawn(Player.WHITE)
        wr = Rook(Player.WHITE)
        wb = Bishop(Player.WHITE)
        wn = Knight(Player.WHITE)
        wq = Queen(Player.WHITE)
        bk = King(Player.BLACK)
        bp = Pawn(Player.BLACK)
        br = Rook(Player.BLACK)
        bb = Bishop(Player.BLACK)
        bn = Knight(Player.BLACK)
        bq = Queen(Player.BLACK)

        self.board = [[wr,wn,wb,wq,wk  ,wb,wn,wr],
                [wp  ,wp  ,wp  ,wp  ,wp  ,wp  ,wp  ,wp  ],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [bp  ,bp  ,bp  ,bp  ,bp  ,bp  ,bp  ,bp  ],
                [br,bn,bb,bq,bk  ,bb,bn,br]]
        self.undo_board = [deepcopy(self.board)]
        self.__player = Player.WHITE
        self.__nrows = 8
        self.__ncols = 8
        self.__message_code = MoveValidity

    @property
    def nrows(self):
        return self.__nrows

    @nrows.setter
    def nrows(self, rows):
        self.__nrows = rows

    @property
    def ncols(self):
        return self.__ncols

    @ncols.setter
    def ncols(self, cols):
        self.__ncols = cols

    @property
    def current_player(self):
        return self.__player

    @current_player.setter
    def current_player(self, Player):
        self.__player = Player

    @property
    def messageCode(self):
        return self.__message_code

    @messageCode.setter
    def messageCode(self, message):
        self.__message_code = message

    def is_complete(self):
        return False

    def is_valid_move(self, move: Move):
        piece = self.board[move.from_row][move.from_col]
        if piece is not None:
            if not isinstance(piece,King):
                if self.in_check(self.current_player()):
                    self.__message_code = MoveValidity.StayingInCheck
                    return False
            if piece.is_valid_move(move,self.board):

                if self.in_check(self.current_player()):
                    self.__message_code = MoveValidity.MovingIntoCheck
                    return False
                else:
                    self.__message_code = MoveValidity.Valid
                    return True

            else:
                self.__message_code = MoveValidity.Invalid
                return False


    def move(self, move: Move):
        piece = self.board[move.from_row][move.from_col]
        self.board[move.from_row][move.from_col] = None
        self.board[move.to_row][move.to_col] = piece
        self.undo_board.append(deepcopy(self.board))
        self.set_next_player()

    def in_check(self,p: Player):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != None:
                    if self.board[y][x].player.name == p.name:
                        if self.board[y][x].type()== 'King':
                            if self.board[y][x].player.name is p.name:
                                kx = x
                                ky = y
        for j in range(len(self.board)):
            for k in range(len(self.board[y])):
                if self.board[j][k] != None:
                    if self.board[j][k].player.name is not p.name:
                            if self.board[j][k].is_valid_move(Move(j, k, ky, kx),self.board):
                                return True
        return False

    def current_player(self):
        return self.__player

    def piece_at(self,row: int, col: int):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]

    def set_next_player(self):
        if self.current_player().name == 'WHITE':
            self.__player = Player.BLACK
        else:
            self.__player = Player.WHITE

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        self.board[row][col] = piece

    def undo(self):
        if len(self.undo_board) == 1:
            raise UndoException
        else:
            del self.undo_board[-1]
            self.board = self.undo_board[-1]


"""
wk = King(Player.WHITE)
wp = Pawn(Player.WHITE)
wr = Rook(Player.WHITE)
bk = King(Player.BLACK)
bp = Pawn(Player.BLACK)
br = Rook(Player.BLACK)
board1 = [[None,None,None,wk,None  ,None,None,None],
                [wp  ,wp  ,wp  ,wp  ,None  ,wp  ,wp  ,wp  ],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [bp  ,bp  ,bp  ,bp  ,br  ,bp  ,bp  ,bp  ],
                [None,None,None,None,bk  ,None,None,None]]
c = ChessModel()
print(c.in_check(Player.WHITE))
move = Move(1,3,3,3)
c.move(move)
print(c.in_check(Player.WHITE))
"""