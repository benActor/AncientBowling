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

    def test_sum_state(self):
        self.assertEqual(15, self.bowling.sum_state([15, "-", "-"]))
        self.assertEqual(0, self.bowling.sum_state(["-", "-", "-"]))
        self.assertEqual(7, self.bowling.sum_state([3, 4, "-"]))

    def test_spare_state(self):
        self.assertFalse(self.bowling.spare_state([3, 7, "-"]))
        self.assertTrue(self.bowling.spare_state([8, 7, "-"]))

    def test_last_frame(self):
        self.assertFalse(self.bowling.last_frame(2, self.bowling.board))

        self.assertTrue(self.bowling.last_frame(4, [[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                    [15, 8, 2, 3]]))

    def test_full_frame(self):
        self.assertFalse(self.bowling.full_frame(frame_pos=1, score_board=[[15, "-", "-"], [7, 6, "-"], ["-", "-", "-"]],
                                                emp_sp_chr="-"))


if __name__ == '__main__':
    main()