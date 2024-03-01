from copy import deepcopy
from enum import Enum
from typing import List
import random
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
        wp0 = Pawn(Player.WHITE)
        wp1 = Pawn(Player.WHITE)
        wp2 = Pawn(Player.WHITE)
        wp3 = Pawn(Player.WHITE)
        wp4 = Pawn(Player.WHITE)
        wp5 = Pawn(Player.WHITE)
        wp6 = Pawn(Player.WHITE)
        wp7 = Pawn(Player.WHITE)
        wr0 = Rook(Player.WHITE)
        wr1 = Rook(Player.WHITE)
        wb0 = Bishop(Player.WHITE)
        wb1 = Bishop(Player.WHITE)
        wn0 = Knight(Player.WHITE)
        wn1 = Knight(Player.WHITE)
        wq0 = Queen(Player.WHITE)
        wq1 = Queen(Player.WHITE)
        bk0 = King(Player.BLACK)
        bk1 = King(Player.BLACK)
        bp0 = Pawn(Player.BLACK)
        bp1 = Pawn(Player.BLACK)
        bp2 = Pawn(Player.BLACK)
        bp3 = Pawn(Player.BLACK)
        bp4 = Pawn(Player.BLACK)
        bp5 = Pawn(Player.BLACK)
        bp6 = Pawn(Player.BLACK)
        bp7 = Pawn(Player.BLACK)
        br0 = Rook(Player.BLACK)
        br1 = Rook(Player.BLACK)
        bb0 = Bishop(Player.BLACK)
        bb1 = Bishop(Player.BLACK)
        bn0 = Knight(Player.BLACK)
        bn1 = Knight(Player.BLACK)
        bq0 = Queen(Player.BLACK)

        self.board = [[br0,bn0,bb0,bq0,bk0  ,bb1,bn1,br1],
                [bp0  ,bp1  ,bp2  ,bp3  ,bp4  ,bp5  ,bp6 ,bp7  ],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [wp0  ,wp1  ,wp2  ,wp3  ,wp4  ,wp5  ,wp6 ,wp7  ],
                [wr0,wn0,wb0,wq0,wk  ,wb1,wn1,wr1]]


        self.__player = Player.WHITE
        self.__nrows = len(self.board)
        self.__ncols = len(self.board[0])
        self.__message_code = MoveValidity
        self.from_list = []
        self.to_list = []
        self.taken_piece = []

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
        if not self.in_check(Player.WHITE) and not self.in_check(Player.BLACK):
            return False
        for x in range(2):
            if self.in_check(self.current_player):
                for y in range(0,8):
                    for x in range(0, 8):
                        if self.board[y][x] is not None:
                            if self.board[y][x].player.name is self.current_player.name:
                                for j in range(0, 8):
                                    for i in range(0, 8):
                                        move = Move(y,x,j,i)
                                        if self.is_valid_move(move):
                                            return False
            self.set_next_player()

        else:
            return True

        return False


    def is_valid_move(self, move: Move):
        piece = self.board[move.from_row][move.from_col]
        if piece is not None:
            if piece.is_valid_move(move, self.board):
                if self.in_check(self.current_player): # staying
                    self.move(move)
                    self.set_next_player()
                    if self.in_check(self.current_player):
                        self.undo()
                        self.set_next_player()
                        self.__message_code = MoveValidity.StayingInCheck
                        return False
                    else:
                        self.undo()
                        self.set_next_player()
                        self.__message_code = MoveValidity.Valid
                        return True
                else:
                    self.move(move)
                    self.set_next_player()
                    if self.in_check(self.current_player): # moving
                        self.undo()
                        self.set_next_player()
                        self.__message_code = MoveValidity.MovingIntoCheck
                        return False
                    else:
                        self.undo()
                        self.set_next_player()
                        self.__message_code = MoveValidity.Valid
                        return True
        self.__message_code = MoveValidity.Invalid
        return False


    def move(self, move: Move):
        piece = self.board[move.from_row][move.from_col]
        temp = []
        temp.append(move.from_row)
        temp.append(move.from_col)
        self.from_list.extend(temp)
        temp = []
        temp.append(move.to_row)
        temp.append(move.to_col)
        self.to_list.extend(temp)
        self.taken_piece.append(self.board[move.to_row][move.to_col])
        self.board[move.from_row][move.from_col] = None
        self.board[move.to_row][move.to_col] = piece
        if move.to_row == 0 or move.to_row == len(self.board)-1:
            if isinstance(self.board[move.to_row][move.to_col],Pawn):
                self.board[move.to_row][move.to_col] = None
                self.board[move.to_row][move.to_col] = Queen(self.current_player)
        self.set_next_player()

    def in_check(self,p: Player):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] != None:
                    if self.board[y][x].player.name == p.name:
                        if self.board[y][x].type()== 'King':
                            kx = x
                            ky = y
        for j in range(len(self.board)):
            for k in range(len(self.board[y])):
                if self.board[j][k] != None:
                    if self.board[j][k].player.name is not p.name:
                            if self.board[j][k].is_valid_move(Move(j, k, ky, kx),self.board):
                                return True
        return False



    def piece_at(self,row: int, col: int):
        if 0 <= row < len(self.board) and 0 <= col < len(self.board):
            return self.board[row][col]

    def set_next_player(self):
        if self.current_player.name == 'WHITE':
            self.__player = Player.BLACK
        else:
            self.__player = Player.WHITE

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        self.board[row][col] = piece

    def undo(self):
        if len(self.from_list) > 0:
            piece = self.board[self.to_list[-2]][self.to_list[-1]]
            self.board[self.to_list[-2]][self.to_list[-1]] = self.taken_piece[-1]
            self.board[self.from_list[-2]][self.from_list[-1]] = piece

            del self.to_list[-2],self.to_list[-1],self.from_list[-2],self.from_list[-1],self.taken_piece[-1]
            self.set_next_player()
        else:
            raise UndoException


    def ai_dumb(self, TF):
        if TF and self.current_player is Player.BLACK:
            while 1:
                if not self.is_complete():
                    row = random.randrange(0,7)
                    col = random.randrange(0,7)
                    if self.board[row][col] is not None:
                        if self.board[row][col].player is Player.BLACK:
                            for y in range(0,8):
                                for x in range(0, 8):
                                    if self.is_valid_move(Move(row,col,y,x)):
                                        self.move(Move(row,col,y,x))
                                        return None
        else:
            return None