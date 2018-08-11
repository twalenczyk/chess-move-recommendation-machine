from enum import Enum, unique

@unique
class Piece_Type(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3
    BISHOP = 4
    KNIGHT = 5
    PAWN = 6
