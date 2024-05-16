from piece_moves_calculator import piece_moves_calculator
from pawn_moves_calculator import pawn_moves_calculator

def piece_possible_moves_getter(piece_type, piece_position, board):

    king_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    bishop_directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (2, 2), (-2, -2), (2, -2), (-2, 2), (3, 3), (-3, -3), (3, -3), (-3, 3), (4, 4), (-4, -4), (4, -4), (-4, 4), (5, 5), (-5, -5), (5, -5), (-5, 5), (6, 6), (-6, -6), (6, -6), (-6, 6), (7, 7), (-7, -7), (7, -7), (-7, 7)]
    rook_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (2, 0), (-2, 0), (0, 2), (0, -2), (3, 0), (-3, 0), (0, 3), (0, -3), (4, 0), (-4, 0), (0, 4), (0, -4), (5, 0), (-5, 0), (0, 5), (0, -5), (6, 0), (-6, 0), (0, 6), (0, -6), (7, 0), (-7, 0), (0, 7), (0, -7)]
    queen_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (2, 2), (-2, -2), (2, -2), (-2, 2), (3, 3), (-3, -3), (3, -3), (-3, 3), (4, 4), (-4, -4), (4, -4), (-4, 4), (5, 5), (-5, -5), (5, -5), (-5, 5), (6, 6), (-6, -6), (6, -6), (-6, 6), (7, 7), (-7, -7), (7, -7), (-7, 7)]
    knight_directions = [(1, 2), (-1, -2), (1, -2), (-1, 2), (2, 1), (-2, -1), (2, -1), (-2, 1)]

    if piece_type.upper() == "K":
        possible_moves = piece_moves_calculator(piece_position, king_directions, board)
    elif piece_type.upper() == "Q":
        possible_moves = piece_moves_calculator(piece_position, queen_directions, board)
    elif piece_type.upper() == "R":
        possible_moves = piece_moves_calculator(piece_position, rook_directions, board)
    elif piece_type.upper() == "B":
        possible_moves = piece_moves_calculator(piece_position, bishop_directions, board)
    elif piece_type.upper() == "N":
        possible_moves = piece_moves_calculator(piece_position, knight_directions, board)
    elif piece_type.upper() == "P":
        possible_moves = pawn_moves_calculator(piece_position, board)

    return possible_moves