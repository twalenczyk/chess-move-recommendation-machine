# Contains information about the board

class Board:

    # attributes
    CONST_NUM_RANKS = 8
    ranks = []

    # methods
    def __init__(self):
        for i in range(self.CONST_NUM_RANKS):
            if i % 2 == 0:
                self.ranks.append('X0X0X0X0')
            else:
                self.ranks.append('0X0X0X0X')

    def print_board(self):
        for i in range(self.CONST_NUM_RANKS):
            print(self.ranks[i])
