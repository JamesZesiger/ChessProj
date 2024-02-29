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

    def is_valid_move(self, move: Move, board):  # deleted type hint
        if move.from_col == move.to_col and move.from_row == move.to_row:
            return False
        elif (move.to_row < 0 or move.to_row > (len(board)-1)) or (move.to_col < 0 or move.to_col > len(board[0])-1):
            return False
        elif board[move.from_row][move.from_col] is not self:
            return False
        elif board[move.to_row][move.to_col] is not None:
            if board[move.to_row][move.to_col].player.name is self.player.name:
                return False
        return True





