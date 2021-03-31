class AncientBowling:

    def __init__(self):
        self.launch, self.frame, self.board = 0, 0, self.create_board("-")

        # true if there was a strike in a frame
        self.strike_state = lambda l: l[0] == 15 and len(l) == 3

        # true if there was a spare in a frame
        self.spare_state = lambda l: self.sum_state(l) == 15 and l[0] < 15 and len(l) == 3

        # true if the frame is at the last position
        self.last_frame = lambda frame, score_board: frame == len(score_board) - 1

    def create_board(self, empty_space_character):
        b = [[empty_space_character for i in range(3)] for j in range(5)]
        b[-1].extend([empty_space_character])
        return b

    """
        Sum integer values in a frame
        :param state: [15, "-", "-"]   ---> frame
        :return: 15
    """
    def sum_state(self, state):
        if not state:
            return 0
        elif isinstance(state[0], int):
            return state[0] + self.sum_state(state[1:])
        else:
            return self.sum_state(state[1:])

    """
        Return True if a frame is complete
         :param frame: 1
         :param score_board: [[15, "-", "-"], [7, 6, "-"], ["-", "-", "-"]]
         :param empty_space: "-"
         :return : False
     """

    def full_frame(self, frame_pos, score_board, emp_sp_chr):
        if self.strike_state(score_board[frame_pos]):
            return True
        if self.spare_state(score_board[frame_pos]):
            return True
        if emp_sp_chr not in score_board[frame_pos]:
            return True
        return False

    """
        Sum first n integer values in the Board and add to 15
        :param n: 3
        :param board: [[15, "-", "-"], [7, 8, "-"], [10, "-", "-"]]
        :return: 45
    """

    def add_n_values(self, n, board):
        count = n
        pin_sum = 0
        for sub_frame in board:
            for value in sub_frame:
                if isinstance(value, int) and count > 0:
                    pin_sum += value
                    count -= 1
        return 15 + pin_sum


    def frame_score(self, frame, pos, board):
        """
        Compute the Score of a frame
        :param frame: [15, "-", "-"]
        :param pos: 0
        :param board: [[15, "-", "-"], [7, 8, "-"], [15, "-", "-"]]
        :return: 45
        """
        if self.strike_state(frame):
            if pos < len(board) - 1:
                return self.add_n_values(3, board[pos + 1:])
            return self.sum_state(frame)
        if self.spare_state(frame):
            if pos < len(board) - 1:
                return self.add_n_values(2, board[pos + 1:])
            else:
                return self.sum_state(frame)
        return self.sum_state(frame)

    def player_score(self, board):
        return sum(self.frame_score(board[i], i, board) for i in range(len(board)))

    def valid_last_frame(self, frame_pos, board, emp_sp_chr):
        """
        to check if a shot is still possible in the last frame
        :param frame_pos: 4
        :param board: [[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                              [5, 8, 1, "-"]]
        :param emp_sp_chr: "-"
        :return: False
        """
        if self.last_frame(frame_pos,  board):
            if emp_sp_chr not in board[frame_pos][:3] and self.sum_state(board[frame_pos][:3]) < 15:
                return False
            if emp_sp_chr not in board[frame_pos]:
                return False
            return True

    def valid_frame(self, frame_pos, board, emp_sp_chr):
        """
        Check if a shot is possible in any frame
        :param frame_pos: 4
        :param board: [[15, "-", "-"], [8, 1, 2], [1, 2, 12], [6, 4, 1],
                                                      [2, 8, 5, "-"]]
        :param emp_sp_chr: "-"
        :return: False
        """
        if self.last_frame(frame_pos, board):
            return self.valid_last_frame(frame_pos, board, emp_sp_chr)
        return emp_sp_chr in board[frame_pos] and self.sum_state(board[frame_pos]) < 14




