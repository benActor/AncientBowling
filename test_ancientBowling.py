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

    def test_valid_frame(self):
        self.assertFalse(self.bowling.valid_frame(1, [[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                      [15, 8, 2, 3]], "-"))

        self.assertTrue(self.bowling.valid_frame(4, [[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                      [2, 8, 5, "-"]], "-"))

    def test_complete_15(self):
        self.assertEqual(0, self.bowling.complete_15([15, 15]))
        self.assertEqual(12, self.bowling.complete_15([8, 4]))
        self.assertEqual(6, self.bowling.complete_15([15, 6]))

    def test_max_next(self):
        self.assertEqual(15, self.bowling.max_next([15, 15]))

        self.assertEqual(8, self.bowling.max_next([15, 3, 4]))

        self.assertEqual(11, self.bowling.max_next([15, 15, 4]))

        self.assertEqual(15, self.bowling.max_next([15, 7, 4, 4]))

        self.assertEqual(14, self.bowling.max_next([1, 0]))

    def test_valid_user_input(self):
        self.assertTrue(self.bowling.valid_user_input(pins=5, frame_pos=3, launch=1, board=[[15, "-", "-"], [8, 1, 2],
                                                                                          [1, 2, 12], [6, 4, "-"],
                                                                                          ["-", "-", "-", "-"]],
                                                      emp_sp_chr="-"))

        self.assertTrue(self.bowling.valid_user_input(pins=0, frame_pos=4, launch=0, board=[[15, "-", "-"], [8, 1, 2],
                                                                                            [1, 2, 12], [6, 4, 5],
                                                                                            ["-", "-", "-", "-"]],
                                                      emp_sp_chr="-"))

        self.assertTrue(self.bowling.valid_user_input(pins=15, frame_pos=4, launch=0, board=[[15, "-", "-"], [8, 1, 2],
                                                                                            [1, 2, 12], [6, 4, 5],
                                                                                            ["-", "-", "-", "-"]],
                                                      emp_sp_chr="-"))

        self.assertTrue(self.bowling.valid_user_input(pins=7, frame_pos=4, launch=2, board=[[15, "-", "-"], [8, 1, 2],
                                                                                             [1, 2, 12], [6, 4, 5],
                                                                                             [15, 8, "-", "-"]],
                                                      emp_sp_chr="-"))

        self.assertFalse(self.bowling.valid_user_input(pins="-", frame_pos=4, launch=2, board=[[15, "-", "-"], [8, 1, 2],
                                                                                            [1, 2, 12], [6, 4, 5],
                                                                                            [15, 8, "-", "-"]],
                                                       emp_sp_chr="-"))

        self.assertFalse(
            self.bowling.valid_user_input(pins="8", frame_pos=4, launch=2, board=[[15, "-", "-"], [8, 1, 2],
                                                                                  [1, 2, 12], [6, 4, 5],
                                                                                  [15, 8, "-", "-"]],
                                          emp_sp_chr="-"))


    def test_shot(self):
        self.assertEqual(15, self.bowling.shot(15))

        self.assertEqual(31, self.bowling.shot(8))

        self.assertEqual(33, self.bowling.shot(1))

        self.assertEqual(37, self.bowling.shot(2))

        self.bowling.shot(1), self.bowling.shot(2)

        self.assertEqual(52, self.bowling.shot(12))

        self.bowling.shot(6), self.bowling.shot(4), self.bowling.shot(1)

        self.assertEqual(73, self.bowling.player_score(self.bowling.board))

        self.assertEqual(88, self.bowling.shot(15))

        self.assertEqual(88, self.bowling.shot("-"))

        self.assertEqual(96, self.bowling.shot(8))

        self.assertEqual(96, self.bowling.shot(15))

        self.assertEqual(98, self.bowling.shot(2))

        self.assertEqual(101, self.bowling.shot(3))


if __name__ == '__main__':
    main()