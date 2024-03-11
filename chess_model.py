"""
This modules purpose is to create the chess game functions
Author: James Zesiger, Quentin Daniere, Evan Bower
Date: 3/11/2024
Version: 1
"""
import random
from enum import Enum
from player import Player
from chess_piece import ChessPiece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from move import Move


class MoveValidity(Enum):
    """
    MoveValidity is an enum class that sets the validity of a move

    Attributes:
        - value(enum): value of the move validity
    """
    Valid = 1
    Invalid = 2
    MovingIntoCheck = 3
    StayingInCheck = 4

    def __str__(self):
        '''
        string override that states reason a move is invalid

        returns: string that states reason the move is invalid
        '''

        if self.value == 2:
            return 'Invalid move.'

        if self.value == 3:
            return 'Invalid -- cannot move into check.'

        if self.value == 4:
            return 'Invalid -- must move out of check.'


# TODO: create UndoException
class UndoException(Exception):
    """
    class that is returned and passed when there is nothing to undo
    """

    pass


class ChessModel:
    """
    class that contains all game methods for chess game to function

    Attributes:
        - board(list(list(chesspiece)): array that contains all pieces on the board
        - __player(enum): current player
        - __nrow(int): number of rows in the board
        - __ncol(int): number of columns in the board
        - __message_code(str): current message that will be displayed
        - from_list(list): list containing all moves from data
        - to_list(list): list containing all moves to data
        - take_piece(list): list of pieces taken each move, includes None
    """

    def __init__(self):
        """
        constructor for ChessModel
        """

        # white piece setup
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
        # black piece setup
        bk0 = King(Player.BLACK)
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

        # board initialization
        self.board = [[br0, bn0, bb0, bq0, bk0, bb1, bn1, br1],
                      [bp0, bp1, bp2, bp3, bp4, bp5, bp6, bp7],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [wp0, wp1, wp2, wp3, wp4, wp5, wp6, wp7],
                      [wr0, wn0, wb0, wq0, wk, wb1, wn1, wr1]]

        self.__player = Player.WHITE  # sets default player to white
        self.__nrows = len(self.board)  # sets number of rows to length of board
        self.__ncols = len(self.board[0])  # sets number of cols to length of board objects
        self.__message_code = MoveValidity  # sets message code to move validity obj
        self.from_list = []  # sets from list to empty list
        self.to_list = []  # sets to list to empty list
        self.taken_piece = []  # sets taken piece to empty list

    @property
    def nrows(self):
        """
        getter for __nrows

        returns: __nrows
        """
        return self.__nrows

    @nrows.setter
    def nrows(self, rows):
        """
        setter for __nrows

        parameters:
            rows(int): new number of rows
        """
        self.__nrows = rows

    @property
    def ncols(self):
        """
        getter for __ncols

        returns: __ncols
        """
        return self.__ncols

    @ncols.setter
    def ncols(self, cols):
        """
        setter for __ncols

        parameters:
            cols(int): new number of columns
        """
        self.__ncols = cols

    @property
    def current_player(self):
        """
        setter for current_player

        returns: __player
        """
        return self.__player

    @current_player.setter
    def current_player(self, Player):
        '''
        setter for current_player

        Parameters:
            Player: new player
        '''
        self.__player = Player

    @property
    def messageCode(self):
        '''
        getter for message_code

        returns: __message_code
        '''
        return self.__message_code

    @messageCode.setter
    def messageCode(self, message):
        '''
        setter for message_code

        parameter:
            message: new message
        '''
        self.__message_code = message

    def is_complete(self):
        '''
        method that checks if any player is in check mate

        returns: bool
        '''
        if not self.in_check(Player.WHITE) and not self.in_check(Player.BLACK):  # if no player is in check
            return False
        for x in range(2):  # repeats for both players
            if self.in_check(self.current_player):  # if current player is in check
                for y in range(0, 8):  # check all rows
                    for x in range(0, 8):  # check all columns
                        if self.board[y][x] is not None:  # if location at y,x is a piece
                            if self.board[y][x].player.name is self.current_player.name:  # if it belongs to current player
                                for j in range(0, 8):
                                    for i in range(0, 8):
                                        move = Move(y, x, j, i)
                                        if self.is_valid_move(move):  # if any piece can move
                                            return False
            self.set_next_player()  # changes player

        else:  # if a player has no moves
            return True

    def is_valid_move(self, move: Move):
        """
        method that checks if a move is valid

        parameter:
            move(Move): contains from data and to data

        returns: bool
        """
        piece = self.board[move.from_row][move.from_col]  # gets piece trying to be moved
        if piece is not None:  # if piece exists
            if piece.is_valid_move(move, self.board):  # checks piece object if the move is valid
                if self.in_check(self.current_player):  # if player is in check
                    self.move(move)  # moves piece
                    self.set_next_player()  # resets player back to current player
                    if self.in_check(self.current_player):  # if player is still in check
                        self.undo()  # undo move
                        self.set_next_player()  # set current player back to player
                        self.__message_code = MoveValidity.StayingInCheck  # sets message code to staying in check value
                        return False  # not valid
                    else:  # player is no longer in check
                        self.undo()  # undoes move
                        self.set_next_player()  # player reset
                        self.__message_code = MoveValidity.Valid  # message code is valid
                        return True  # move is valid
                else:  # player is not in check
                    self.move(move)  # moves piece
                    self.set_next_player()  # resets player
                    if self.in_check(self.current_player):  # if player is in check
                        self.undo() # undoes move
                        self.set_next_player()  # resets player
                        self.__message_code = MoveValidity.MovingIntoCheck  # message code is moving into check val
                        return False  # move invalid
                    else:  # player is not in check
                        self.undo()
                        self.set_next_player()
                        self.__message_code = MoveValidity.Valid  # valid message
                        return True  # valid move
        self.__message_code = MoveValidity.Invalid  # if not valid move is invalid
        return False  # invalid

    def move(self, move: Move):
        """
        method that moves piece
        parameters:
            move(Move): from and to data
        """
        piece = self.board[move.from_row][move.from_col]  # gets piece object at from location
        temp = [move.from_row, move.from_col]  # temp list of from locations
        self.from_list.extend(temp)  # add list of locations to from list
        temp = [move.to_row, move.to_col]  # temp list of to locations
        self.to_list.extend(temp)  # add list of locations to to_list
        self.taken_piece.append(self.board[move.to_row][move.to_col])  # add object take to taken list
        self.board[move.from_row][move.from_col] = None  # sets piece location to None
        self.board[move.to_row][move.to_col] = piece  # sets to location to piece being moved
        if move.to_row == 0 or move.to_row == len(self.board) - 1:  # if piece is on final row
            if isinstance(self.board[move.to_row][move.to_col], Pawn):  # if piece being moved is a queen
                self.board[move.to_row][move.to_col] = None
                self.board[move.to_row][move.to_col] = Queen(self.current_player)  # piece is now queen
        self.set_next_player()  # changes players

    def in_check(self, p: Player):
        """
        method that check if player is in check
        parameter:
            p: player being checked

        return: bool
        """
        for y in range(len(self.board)):
            for x in range(len(self.board[y])): # looks for king location
                if self.board[y][x] != None:
                    if self.board[y][x].player.name == p.name:
                        if self.board[y][x].type() == 'King':
                            kx = x  # king col
                            ky = y  # king row
        for j in range(len(self.board)):
            for k in range(len(self.board[y])):  # checks if opposing player can make a valid move to king location
                if self.board[j][k] != None:
                    if self.board[j][k].player.name is not p.name:
                        if self.board[j][k].is_valid_move(Move(j, k, ky, kx), self.board):
                            return True  # king is in check
        return False  # king is not in check

    def piece_at(self, row: int, col: int):
        """
        method that get piece at a location

        parameters:
            row(int): row
            col(int): col

        return: self.board[row][col] (obj at row,col)
        """
        if 0 <= row < len(self.board) and 0 <= col < len(self.board):  # if in range of board
            return self.board[row][col]

    def set_next_player(self):
        """
        method that sets next player
        """

        if self.current_player.name == 'WHITE':  # if current player is WHITE
            self.__player = Player.BLACK
        else:  # if current player is BLACK
            self.__player = Player.WHITE

    def set_piece(self, row: int, col: int, piece: ChessPiece):
        """
        method that sets a piece at a desired location
        parameter
            row: row location
            col: column location
            piece:  desired piece object
        """
        self.board[row][col] = piece

    def undo(self):
        """
        method that undoes last move

        raise: UndoExeption when no moves can be undone
        """
        if len(self.from_list) > 0:  # if there are any moves that can be undone
            piece = self.board[self.to_list[-2]][self.to_list[-1]]  # get piece last moved
            self.board[self.to_list[-2]][self.to_list[-1]] = self.taken_piece[-1]  # sets location of last piece
                                                                                   # moved to piece that was taken
            self.board[self.from_list[-2]][self.from_list[-1]] = piece  # sets moved piece to previous location

            del self.to_list[-2], self.to_list[-1], self.from_list[-2], self.from_list[-1], self.taken_piece[-1]
            # remove move from lists
            self.set_next_player()  # sets player to previous player
        else:  # if no move to be undone
            raise UndoException

    def ai_dumb(self, TF):
        """
        method that playes game for black player
        parameters:
            TF: True or False

        returns: None
        """

        if TF and self.current_player is Player.BLACK:  # if ai is on
            if not self.is_complete():  # if not in checkmate
                while 1:  # loop until move is found
                    row = random.randrange(0, 7)
                    col = random.randrange(0, 7)
                    if self.board[row][col] is not None:
                        if self.board[row][col].player is Player.BLACK: # pick random black piece
                            y = random.randrange(0, 7)
                            x = random.randrange(0, 7)
                            if self.is_valid_move(Move(row, col, y, x)):  # does random move
                                self.move(Move(row, col, y, x))
                                return None

        else:  # if player is not black
            return None
