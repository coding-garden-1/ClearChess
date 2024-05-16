
def piece_moves_calculator(king_position, piece_directions, board):
    king_row, king_col = king_position
    possible_moves = []
    
    # Check all 8 possible directions for king movement
    # Define the possible directions for king movement

    for direction in piece_directions:
        # Get the x and y vectors from the possible move
        x_move, y_move = direction
        
        # Calculate the new position by adding the offsets to the current position
        new_row = king_row + y_move
        new_col = king_col + x_move
        
        # Check if the new position is within the board boundaries
        
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] == '':
                possible_moves.append((new_row, new_col))
    return possible_moves
