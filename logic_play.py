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
    
    pieces = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
    
    for row in range(8):
        chessboard += '<tr>'
        
        for col in range(8):
            if (row + col) % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            
            if row == 0 or row == 7:
                piece = pieces[col]
            elif row == 1 or row == 6:
                piece = '♟' if row == 1 else '♙'
            else:
                piece = ''
            
            chessboard += '<td style="width: 50px; height: 50px; background-color: {};">{}</td>'.format(color, piece)
        
        chessboard += '</tr>'
    
    chessboard += '</table></body></html>'
    return chessboard

# Generate the chessboard HTML and save it to a file
chessboard_html = generate_chessboard()

with open('chessboard.html', 'w') as file:
    file.write(chessboard_html)
