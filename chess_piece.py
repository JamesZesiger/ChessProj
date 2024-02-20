from abc import ABC, abstractmethod
from typing import List
from enum import Enum
from move import Move


class ChessPiece(ABC):
    def __init__(self, Player: Enum):
        self.__player = Player

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, nplayer):
        self.__player = nplayer

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def type(self):
        pass

    def is_valid_move(self, move: Move, board):  #deleted type hint
        if move.from_col == move.to_col and move.from_row == move.to_row:
            return False
        elif not 0 <= move.to_row <= 8 or 0 <= move.to_col <= 8:
            return False
        elif board[move.from_row][move.from_col] != None:
            pass





