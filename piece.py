# Contains information about a piece
from piece_type_enum import Piece_Type
from color_enum import Color_Type

class Piece:

    # attributes
    color = Color_Type.WHITE
    piece_type = Piece_Type.PAWN
    x_cord = 0
    y_cord = 0
    rep = ''

    # methods
    def __init__(self, color, ptype):
        self.set_color(color)
        self.set_type(ptype)
        self.set_rep()

    # def __repr__(self):
    #     print('{color: '+str(self.color)+'type: '+str(self.piece_type)+'at: ('+str(self.x_cord)+','+str(self.y_cord)+')}')

    def set_color(self, color):
        if color == 'white':
            self.color = Color_Type.WHITE
        else:
            self.color = Color_Type.BLACK

    def set_type(self, ptype):
        if ptype == 'king':
            self.piece_type = Piece_Type.KING
        elif ptype == 'queen':
            self.piece_type = Piece_Type.QUEEN
        elif ptype == 'rook':
            self.piece_type = Piece_Type.ROOK
        elif ptype == 'bishop':
            self.piece_type = Piece_Type.BISHOP
        elif ptype == 'knight':
            self.piece_type = Piece_Type.KNIGHT
        else:
            self.piece_type = Piece_Type.PAWN

    def set_x_cord(self, cord):
        self.x_cord = cord

    def set_y_cord(self, cord):
        self.y_cord = cord

    def set_rep(self):
        col = ''
        p = ''
        if self.color == Color_Type.WHITE:
            col = 'w'
        else:
            col = 'b'

        if self.piece_type == Piece_Type.KING:
            p ='K'
        elif self.piece_type == Piece_Type.QUEEN:
            p = 'Q'
        elif self.piece_type == Piece_Type.ROOK:
            p = 'R'
        elif self.piece_type == Piece_Type.BISHOP:
            p = 'B'
        elif self.piece_type == Piece_Type.KNIGHT:
            p = 'N'
        else:
            p = 'P'

        self.rep = col + p

    def get_x_cord(self):
        return self.x_cord

    def get_y_cord(self):
        return self.y_cord

    def get_rep(self):
        return self.rep
