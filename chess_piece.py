from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from move import Move


class ChessPiece(ABC):
    """
    This is the Parent class for all types of pieces and holds the default formatting and properties for
    the children classes that will be created.
    """
    def __init__(self, Player: Enum):
        """
        Initializes the piece as a color
        :param Player: The color of the piece
        """
        self.__player = Player

    @property
    def player(self):
        """
        Player property getter
        :return: the player color and piece as enum
        """
        return self.__player

    @player.setter
    def player(self, nplayer):
        """
        The player setter property
        :param nplayer: new player color desired
        :return: none
        """
        self.__player = nplayer

    @abstractmethod
    def __str__(self):
        """
        Abstract method for the string returned by the class.
        :return: pass
        """
        pass

    @abstractmethod
    def type(self):
        """
        Abstract method to see the type of piece that the object will be
        :return: pass
        """
        pass

    def is_valid_move(self, move: Move, board):  # deleted type hint
        """
        This method checks whether the chosen piece can be moved to the target position.
        This is the default check that each piece will need, each individual piece also has a custom validation for
        their individual movement.
        The move class from location must match to a piece on the board in order to process
        :param move: move class input, contains from_col, from_row, to_col, and to_row
        :param board: the 8 by 8 chess board with pieces to choose from.
        :return: True or False depending on validity of movement
        """
        if move.from_col == move.to_col and move.from_row == move.to_row:
            # Check that move is to a new location
            return False
        elif (move.to_row < 0 or move.to_row > (len(board)-1)) or (move.to_col < 0 or move.to_col > len(board[0])-1):
            # Check that the move is within the confines of the board
            return False
        elif board[move.from_row][move.from_col] is not self:
            # Check that the starting location is your own piece
            return False
        elif board[move.to_row][move.to_col] is not None:
            # Check target location
            if board[move.to_row][move.to_col].player.name is self.player.name:
                # Check whether target location is yourself
                return False
        return True





