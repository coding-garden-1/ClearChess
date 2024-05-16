
def pawn_moves_calculator(pawn_position, board):
    king_row, king_col = pawn_position
    possible_moves = []
    
    # Check all 8 possible directions for king movement
    # Define the possible directions for king movement
    move_directions = [(0,1), (0,2)]
    capture_directions = [(1,1), (-1,1)]
    
    for direction in move_directions:
        # Get the x and y vectors from the possible move
        x_move, y_move = direction
        
        # Calculate the new position by adding the offsets to the current position
        new_row = king_row + y_move
        new_col = king_col + x_move
        
        # Check if the new position is within the board boundaries

        if 0 <= new_row < 8 and 0 <= new_col < 8:

            possible_moves.append((new_row, new_col))

    for direction in capture_directions:
        # Get the x and y vectors from the possible move
        x_move, y_move = direction
        
        # Calculate the new position by adding the offsets to the current position
        new_row = king_row + y_move
        new_col = king_col + x_move
        
        # Check if the new position is within the board boundaries

        if 0 <= new_row < 8 and 0 <= new_col < 8:
            if board[new_row][new_col] != '':

                possible_moves.append((new_row, new_col))
    
    return possible_moves
