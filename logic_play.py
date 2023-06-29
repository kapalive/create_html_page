# In this updated version, we have added the chess pieces as Unicode characters. The pieces are stored in the pieces list, which represents the initial arrangement of the pieces on the board.
#The logic for placing the pieces on the board is as follows:
#The first and last rows (row == 0 or row == 7) represent the back rows where the 
# rooks (♜), knights (♞), bishops (♝), queen (♛), king (♚), and bishops (♝), knights (♞), and rooks (♜) are placed in order.
#The second and second-to-last rows (row == 1 or row == 6) represent the rows of pawns (♟ for black pawns and ♙ for white pawns).
#For all other rows, the empty string is used to represent the absence of a piece.
#When you run this code and open the generated chessboard.html file in a web browser, you will see the chessboard with the pieces arranged according to the initial setup of a standard chess game.


def generate_chessboard():
    chessboard = '<html><head><title>Chessboard</title></head><body>'
    chessboard += '<table style="border-collapse: collapse;">'

    pieces = [
        '♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜',
        '♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟',
        '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '',
        '', '', '', '', '', '', '', '',
        '♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙',
        '♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'
    ]

    for row in range(8):
        chessboard += '<tr>'

        for col in range(8):
            if (row + col) % 2 == 0:
                color = 'white'
            else:
                color = 'black'

            piece = pieces[row * 8 + col]

            chessboard += '<td style="width: 50px; height: 50px; background-color: {};">{}</td>'.format(color, piece)

        chessboard += '</tr>'

    chessboard += '</table></body></html>'
    return chessboard


# Function to check if a move is within the chessboard bounds
def is_valid_move(row, col):
    return 0 <= row < 8 and 0 <= col < 8


# Function to check if a move is valid for a pawn
def is_valid_pawn_move(row, col, target_row, target_col, piece):
    if piece == '♟':  # Black pawn
        return target_col == col and target_row == row + 1
    elif piece == '♙':  # White pawn
        return target_col == col and target_row == row - 1
    return False


# Function to check if a move is valid for a rook
def is_valid_rook_move(row, col, target_row, target_col):
    return row == target_row or col == target_col


# Function to check if a move is valid for a knight
def is_valid_knight_move(row, col, target_row, target_col):
    row_diff = abs(target_row - row)
    col_diff = abs(target_col - col)
    return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)


# Function to check if a move is valid for a bishop
def is_valid_bishop_move(row, col, target_row, target_col):
    return abs(target_row - row) == abs(target_col - col)


# Function to check if a move is valid for a queen
def is_valid_queen_move(row, col, target_row, target_col):
    return is_valid_rook_move(row, col, target_row, target_col) or \
           is_valid_bishop_move(row, col, target_row, target
