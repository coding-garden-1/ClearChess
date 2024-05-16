
def move_validator(piece_position, new_position, possible_moves):
    if piece_position - new_position in possible_moves:
        return piece_position - new_position
