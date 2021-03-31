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

    def test_add_n_values(self):
        self.assertEqual(45, self.bowling.add_n_values(3, [[15, "-", "-"], [7, 8, "-"], [15, "-", "-"]]))
        self.assertEqual(39, self.bowling.add_n_values(2, [[15, "-", "-"], [9, 6, "-"], [15, "-", "-"]]))
        self.assertEqual(30, self.bowling.add_n_values(1, [[15, "-", "-"], [7, 8, "-"], [15, "-", "-"]]))

    def test_frame_score(self):
        self.assertEqual(44, self.bowling.frame_score([15, "-", "-"], 0, [[15, "-", "-"], [7, 8, "-"], [14, 1, "-"]]))
        self.assertEqual(11, self.bowling.frame_score([1, 7, 3], 1, [[15, "-", "-"], [1, 7, 3], [14, 1, "-"]]))
        self.assertEqual(6, self.bowling.frame_score([1, 2, 3], 1, [[1, 2, 3], [7, 8, "-"], [14, 1, "-"]]))

    def test_player_score(self):
        self.assertEqual(300, self.bowling.player_score([[15, "-", "-"], [15, "-", "-"], [15, "-", "-"], [15, "-", "-"],
                                                         [15, 15, 15, 15]]))

        self.assertEqual(101, self.bowling.player_score([[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                         [15, 8, 2, 3]]))

        self.assertEqual(21, self.bowling.player_score([[1, 2, 3], [15, "-", "-"]]))
        self.assertEqual(45, self.bowling.player_score([[1, 2, 3], [15, "-", "-"], [8, 1, 3]]))

    def test_valid_last_frame(self):
        self.assertFalse(self.bowling.valid_last_frame(frame_pos=4, board=[[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                    [15, 8, 2, 3]], emp_sp_chr="-"))

        self.assertTrue(self.bowling.valid_last_frame(frame_pos=4, board=[[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                         [15, 8, "-", "-"]], emp_sp_chr="-"))

        self.assertTrue(
            self.bowling.valid_last_frame(frame_pos=4, board=[[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                              [5, 8, 2, "-"]], emp_sp_chr="-"))

        self.assertFalse(
            self.bowling.valid_last_frame(frame_pos=4, board=[[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                              [5, 8, 1, "-"]], emp_sp_chr="-"))

if __name__ == '__main__':
    main()