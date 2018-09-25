import unittest

from randompath import Direction, _is_legal_move


class IllegalTurnTest(unittest.TestCase):

    def test_must_be_illegal(self):
        self.assertFalse(_is_legal_move([Direction.Direction.LEFT, Direction.Direction.LEFT], Direction.Direction.RIGHT))
        self.assertFalse(_is_legal_move([Direction.UP, Direction.RIGHT], Direction.Direction.LEFT))
        self.assertFalse(_is_legal_move([Direction.UP, Direction.LEFT], Direction.Direction.RIGHT))

    def test_must_be_legal(self):
        self.assertTrue(_is_legal_move([Direction.LEFT, Direction.LEFT], Direction.LEFT))
        self.assertTrue(_is_legal_move([Direction.RIGHT, Direction.RIGHT], Direction.RIGHT))
        self.assertTrue(_is_legal_move([Direction.LEFT, Direction.UP, Direction.UP], Direction.LEFT))
        self.assertTrue(_is_legal_move([Direction.RIGHT, Direction.UP, Direction.UP], Direction.LEFT))
        self.assertTrue(_is_legal_move([Direction.LEFT, Direction.UP, Direction.UP], Direction.RIGHT))
        self.assertTrue(_is_legal_move([Direction.UP, Direction.UP, Direction.UP], Direction.UP))
