import unittest

from labyrinth import UP, RIGHT, LEFT, would_be_illegal_turn


class IllegalTurnTest(unittest.TestCase):

    def test_must_be_illegal(self):
        self.assertTrue(would_be_illegal_turn(RIGHT, [LEFT, LEFT]))
        self.assertTrue(would_be_illegal_turn(LEFT, [UP, RIGHT]))
        self.assertTrue(would_be_illegal_turn(RIGHT, [UP, LEFT]))

    def test_must_be_legal(self):
        self.assertFalse(would_be_illegal_turn(LEFT, [LEFT, LEFT]))
        self.assertFalse(would_be_illegal_turn(RIGHT, [RIGHT, RIGHT]))
        self.assertFalse(would_be_illegal_turn(LEFT, [LEFT, UP, UP]))
        self.assertFalse(would_be_illegal_turn(LEFT, [RIGHT, UP, UP]))
        self.assertFalse(would_be_illegal_turn(RIGHT, [LEFT, UP, UP]))
        self.assertFalse(would_be_illegal_turn(UP, [UP, UP, UP]))
