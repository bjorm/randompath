import unittest

from randompath import UP, RIGHT, LEFT, is_legal_move


class IllegalTurnTest(unittest.TestCase):

    def test_must_be_illegal(self):
        self.assertFalse(is_legal_move([LEFT, LEFT], RIGHT))
        self.assertFalse(is_legal_move([UP, RIGHT], LEFT))
        self.assertFalse(is_legal_move([UP, LEFT], RIGHT))

    def test_must_be_legal(self):
        self.assertTrue(is_legal_move([LEFT, LEFT], LEFT))
        self.assertTrue(is_legal_move([RIGHT, RIGHT], RIGHT))
        self.assertTrue(is_legal_move([LEFT, UP, UP], LEFT))
        self.assertTrue(is_legal_move([RIGHT, UP, UP], LEFT))
        self.assertTrue(is_legal_move([LEFT, UP, UP], RIGHT))
        self.assertTrue(is_legal_move([UP, UP, UP], UP))
