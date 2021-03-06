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

    def sum_state(self, state):
        """
        Sum integer values in a frame
        :param state: [15, "-", "-"]
        :return: 15
        """
        if not state:
            return 0
        elif isinstance(state[0], int):
            return state[0] + self.sum_state(state[1:])
        else:
            return self.sum_state(state[1:])



    def add_n_values(self, n, board):
        """
        Sum first n integer values in the Board and add to 15
        :param n: 3
        :param board: [[15, "-", "-"], [7, 8, "-"], [10, "-", "-"]]
        :return: 45
        """
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
        return emp_sp_chr in board[frame_pos] and self.sum_state(board[frame_pos]) <= 14

    def complete_15(self, l):
        """

        :param l: [8, 4]
        :return: 12
        """
        if not l:
            return 0
        elif l[0] == 15:
            return self.complete_15(l[1:])
        else:
            return l[0] + self.complete_15(l[1:])

    def max_next(self, l):
        """
        Computes the maximum pins score for the next launch
        :param l: [1, 0]
        :return: 14
        """
        if sum(l) == 15:
            max_val = 15
        else:
            max_val = 15 - self.complete_15(l)
        return max_val if max_val else 15

    def valid_user_input(self, pins, frame_pos, launch, board, emp_sp_chr):
        """
        True if the user input is valid in term of type and possible pins
        :param pins: "-"
        :param frame_pos: 4
        :param launch: 2
        :param board: [[15, "-", "-"], [8, 1, 2],[1, 2, 12], [6, 4, 5],[15, 8, "-", "-"]]
        :param emp_sp_chr: "-"
        :return: False
        """
        if isinstance(pins, int):
            if self.last_frame(frame_pos, board) and self.valid_frame(frame_pos, board, "-"):
                return pins <= self.max_next(board[frame_pos][:launch])
            if self.valid_frame(frame_pos, board, emp_sp_chr) :
                return self.sum_state(board[frame_pos]) + pins <= 15
        return False

    def shot(self, pins):
        """
        Register pins shoot and compute the score of the player
        :param pins: 15
        :return: 15
        """
        result = self.player_score(self.board)
        if self.valid_user_input(pins, self.frame, self.launch, self.board, "-"):
            self.board[self.frame][self.launch] = pins
            result = self.player_score(self.board)
            print(self.board)

            if self.valid_frame(self.frame, self.board, "-") and not self.last_frame(self.frame, self.board):
                self.launch += 1
            elif not self.valid_frame(self.frame, self.board, "-") and not self.last_frame(self.frame, self.board):
                self.frame += 1
                self.launch = 0
            elif self.valid_frame(self.frame, self.board, "-") and self.last_frame(self.frame,
                                                                                      self.board) and self.launch < 2:
                self.launch += 1
            elif self.valid_frame(self.frame, self.board, "-") and self.last_frame(self.frame,
                                                                                      self.board) and self.launch == 2 and self.sum_state(
                    self.board[self.frame]) >= 15:
                self.launch += 1
            else:
                self.launch = 0
                self.frame = 0
                self.board = self.create_board("-")
        return result




