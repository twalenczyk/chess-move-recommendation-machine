# Contains information about the board

class Board:

    # attributes
    CONST_NUM_RANKS = 8
    ranks = []

    # methods
    def __init__(self, pieces):
        # generate board
        self.ranks = [
                    [
                        '' for _ in range(self.CONST_NUM_RANKS)
                        ]
                    for _ in range(self.CONST_NUM_RANKS)
                ]

        # add pieces
        for piece in pieces:
            x_cord = piece.x_cord % 64
            y_cord = piece.y_cord % 64
            self.ranks[x_cord][y_cord] = piece.get_rep()

    def print_board(self):
        for rank in self.ranks:
            print(rank)
