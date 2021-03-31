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



