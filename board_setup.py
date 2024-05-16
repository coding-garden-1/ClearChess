import tkinter as tk

def board_setup():
    board = {
        "1": ["r","n",'b','k','q','b','n','r'],
        "2": ['p','p','p','p','p','p','p','p'],
        "3": ['','','','','','','',''],
        "4": ['','','','','','','',''],
        "5": ['','','','','','','',''],
        "6": ['','','','','','','',''],
        "7": ['P','P','P','P','P','P','P','P'],
        "8": ['R','N','B','K','Q','B','N','R']
    }
    return board

def get_team_pieces(team):
    
    if team == "black":
        
        return ['R','N','B','K','Q','P']
    
    else:

        return ['r','n','b','k','q','p']

def interact_with_chess_board():
    board = board_setup()
    team_pieces = get_team_pieces()  # Assuming you have a function to get team pieces

    root = tk.Tk()
    root.title("Chess Board")

    ####################### handle move-making logic ##############################################   

    chosen_piece = None  # Initialize chosen_piece in the outer scope

    def button_clicked(row, col, team_pieces):
        nonlocal chosen_piece  # Declare chosen_piece as nonlocal to modify it within this function
        if board[str(row+1)][col] in team_pieces:
            chosen_piece = board[str(row+1)][col]
            # Update some state or UI here if necessary
        else:
            if chosen_piece:  # Ensure chosen_piece is not None before making a move
                chosen_move = move_validator((row, col))
                make_move_on_board(chosen_move, chosen_piece, board)
                chosen_piece = None  # Reset chosen_piece after the move

    ##########################################################################

    for row in range(8):
        for col in range(8):
            button = tk.Button(root, width=5, height=2, command=lambda r=row, c=col: button_clicked(r, c, team_pieces))
            button.grid(row=row, column=col)
            button.config(text=board[str(row+1)][col])

    root.mainloop()

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


def piece_to_movements(piece_type, piece_position, board):

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

def move_validator(piece_position, new_position, possible_moves):
    if piece_position - new_position in possible_moves:
        return piece_position - new_position

def make_move_on_board(chosen_move, board, piece_position, new_position):
    piece_x, piece_y = piece_position
    new_x, new_y = new_position
    board[piece_x][piece_y] = ''

    
    board[]