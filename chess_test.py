
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
import chess_model
import unittest

import king


class Test_ChessGame(unittest.TestCase):

    def test_rook_checkmate(self):
        game = chess_model.ChessModel()
        for y in range(0,8):
            for x in range(0, 8):
                game.set_piece(y,x,None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(0, 7, Rook(Player.WHITE))
        game.set_piece(1, 7, Rook(Player.WHITE))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_complete(),'Rook Check Mate')

    def test_queen_checkmate(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(1, 1, Queen(Player.WHITE))
        game.set_piece(2, 2, King(Player.WHITE))
        self.assertTrue(game.is_complete(), 'Queen Check Mate')

    def test_knight_checkmate(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(2, 1, Knight(Player.WHITE))
        game.set_piece(1, 2, King(Player.WHITE))
        game.set_piece(2, 2, Knight(Player.WHITE))
        self.assertTrue(game.is_complete(), 'Knight Check Mate')

    def test_bishop_checkmate(self):
        game = chess_model.ChessModel()
        for y in range(0,8):
            for x in range(0, 8):
                game.set_piece(y,x,None)
        game.set_piece(0, 6, King(Player.BLACK))
        game.set_piece(1, 6, Bishop(Player.WHITE))
        game.set_piece(2, 6, King(Player.WHITE))
        game.set_piece(3, 3, Bishop(Player.WHITE))
        self.assertTrue(game.is_complete(),'Bishop Check Mate')

    def test_pawn_checkmate(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(1, 1, Pawn(Player.WHITE))
        game.set_piece(1, 2, Pawn(Player.WHITE))
        game.set_piece(2, 1, King(Player.WHITE))
        self.assertTrue(game.is_complete(), 'Pawn Check Mate')

    def test_pawn_checkmateW(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(7, 7, King(Player.WHITE))
        game.set_piece(6, 6, Pawn(Player.BLACK))
        game.set_piece(6, 5, Pawn(Player.BLACK))
        game.set_piece(5, 6, King(Player.BLACK))
        self.assertTrue(game.is_complete(), 'Pawn white Check Mate')
if __name__ == '__main__':
    unittest.main()