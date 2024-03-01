
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

    def test_rook_invalid(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(3, 6, Rook(Player.WHITE))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertFalse(game.is_valid_move(Move(3,6,4,5)),'Rook invalid move')

    def test_rook_take_blocked_vert(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(6, 3, Rook(Player.WHITE))
        game.set_piece(4, 3, Pawn(Player.BLACK))
        game.set_piece(3, 3, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertFalse(game.is_valid_move(Move(6,3,3,3)),'Rook take blocked vert')

    def test_rook_take_vert_multi(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(6, 3, Rook(Player.WHITE))
        game.set_piece(3, 3, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_valid_move(Move(6,3,3,3)),'Rook take vert multi')

    def test_rook_take_vert_single(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(6, 3, Rook(Player.WHITE))
        game.set_piece(5, 3, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_valid_move(Move(6,3,5,3)),'Rook take vert single')

    def test_rook_take_blocked_horz(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(3, 6, Rook(Player.WHITE))
        game.set_piece(3, 4, Pawn(Player.BLACK))
        game.set_piece(3, 2, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertFalse(game.is_valid_move(Move(3,6,3,2)),'Rook take blocked horz')

    def test_rook_take_horz_multi(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(3, 6, Rook(Player.WHITE))
        game.set_piece(3, 2, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_valid_move(Move(3,6,3,2)),'Rook take horz multi')

    def test_rook_take_horz_single(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(3, 6, Rook(Player.WHITE))
        game.set_piece(3, 5, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_valid_move(Move(3,6,3,5)),'Rook take horz single')

    def test_bishop_take_blocked(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(0, 7, Bishop(Player.WHITE))
        game.set_piece(5, 2, Pawn(Player.BLACK))
        game.set_piece(6, 1, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertFalse(game.is_valid_move(Move(0, 7, 6, 1)), 'bishop take blocked')

    def test_bishop_take(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(0, 7, Bishop(Player.WHITE))
        game.set_piece(6, 1, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_valid_move(Move(0, 7, 6, 1)), 'bishop take')

    def test_pawn_take(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(5, 2, Pawn(Player.BLACK))
        game.set_piece(6, 1, Pawn(Player.WHITE))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertTrue(game.is_valid_move(Move(6, 1, 5, 2)), 'pawn take')
        self.assertTrue(game.is_valid_move(Move(5, 2, 6, 1)), 'pawn take')

    def test_pawn_valid_move(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(1, 1, Pawn(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        for x in range(2,4):
            self.assertTrue(game.is_valid_move(Move(1, 1, x, 1)), 'pawn take')

    def test_knight(self):
        game = chess_model.ChessModel()
        for y in range(0, 8):
            for x in range(0, 8):
                game.set_piece(y, x, None)
        game.set_piece(0, 0, King(Player.BLACK))
        game.set_piece(3, 3, Knight(Player.WHITE))
        game.set_piece(2, 5, Knight(Player.WHITE))
        game.set_piece(1, 4, Knight(Player.BLACK))
        game.set_piece(7, 7, King(Player.WHITE))
        self.assertFalse(game.is_valid_move(Move(3, 3, 2, 5)), 'Knight takes same team take')
        self.assertTrue(game.is_valid_move(Move(3, 3, 1, 4)), 'Knight takes opp team take')
        self.assertTrue(game.is_valid_move(Move(3, 3, 1, 2)), 'Knight moves')

if __name__ == '__main__':
    unittest.main()