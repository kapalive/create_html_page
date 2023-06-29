# When you run this code, it will create an HTML file named chessboard.html in the same directory as your Python script. The file will contain the HTML code for the chessboard.

# Each square of the chessboard is represented by a <td> (table data) element with a width and height of 50 pixels. 
# The background color of each square is determined by the color variable, which alternates between "white" and "black" based on the position of the square.

def generate_chessboard():
    chessboard = '<html><head><title>Chessboard</title></head><body>'
    chessboard += '<table style="border-collapse: collapse;">'
    
    for row in range(8):
        chessboard += '<tr>'
        
        for col in range(8):
            if (row + col) % 2 == 0:
                color = 'white'
            else:
                color = 'black'
            
            chessboard += '<td style="width: 50px; height: 50px; background-color: {};"></td>'.format(color)
        
        chessboard += '</tr>'
    
    chessboard += '</table></body></html>'
    return chessboard

# Generate the chessboard HTML and save it to a file
chessboard_html = generate_chessboard()

with open('chessboard.html', 'w') as file:
    file.write(chessboard_html)
