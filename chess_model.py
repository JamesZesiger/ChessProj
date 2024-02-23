from enum import Enum
from typing import List

import move
from player import Player
from move import Move
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
#from knight import Knight
#from bishop import Bishop
#from queen import Queen
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


class ChessModel:
    def __init__(self,board: List[List[ChessPiece]], Player: Enum, rows: int, cols: int, MoveValidity: Enum):
        self.board = board
        self.__player = Player
        self.__nrows = rows
        self.__ncols = cols
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

    def is_compleate(self):
        pass

    def is_valid_move(self):
        pass

    def move(self, move: Move):
        pass

    def in_check(self,p: Player):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != None:
                    if self.board[y][x].player.name == p.name:
                        if self.board[y][x].type()== 'king':
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
        pass

    def piece_at(self,row: int, col: int):
        pass

    def set_next_player(self):
        pass

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        pass

    def undo(self):
        pass

wk = King(Player.WHITE)
wp = Pawn(Player.WHITE)
wr = Rook(Player.WHITE)
bk = King(Player.BLACK)
bp = Pawn(Player.BLACK)
br = Rook(Player.BLACK)
board = [[None,None,None,None,wk  ,None,None,None],
                [wp  ,wp  ,wp  ,wp  ,wr  ,wp  ,wp  ,wp  ],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [bp  ,bp  ,bp  ,bp  ,bp  ,bp  ,bp  ,bp  ],
                [None,None,None,None,bk  ,None,None,None]]
c = ChessModel(board,Player.WHITE,8,8,MoveValidity)
print(c.in_check(Player.BLACK))
m = Move(1,4,2,3)
print(wr.is_valid_move(m,board))