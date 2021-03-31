from unittest import TestCase, main
from ancientBowling import AncientBowling


class AncientBowlingTest(TestCase):
    def setUp(self):
        self.bowling = AncientBowling()

    def test_bowling_class(self):
        self.assertIsInstance(self.bowling, AncientBowling)

    def test_create_board(self):
        self.assertEqual([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-", "-"]]
                         , self.bowling.create_board("-"))

    def test_strike_state(self):
        self.assertTrue(self.bowling.strike_state([15, "-", "-"]))
        self.assertFalse(self.bowling.strike_state([15, "-", "-", "-"]))

    def test_spare_state(self):
        self.assertFalse(self.bowling.spare_state([3, 7, "-"]))
        self.assertTrue(self.bowling.spare_state([8, 7, "-"]))


if __name__ == '__main__':
    main()