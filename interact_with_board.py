
def interact_with_chess_board(board):
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
