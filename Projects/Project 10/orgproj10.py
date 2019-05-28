import reversi
import string
from operator import itemgetter
LETTERS = string.ascii_lowercase

"""
Write something about this program here.
"""

def indexify(position):
    """
    Coverts letter-number position to row-column indices and returns in the 
    form of a tuple. 
    """
    row_dict = {}
    for cha, val in enumerate(LETTERS, 0):
        row_dict[val] = cha
    return (row_dict[position[0]], int(position[1:])-1) # are these supposed to be strings?

def deindexify(row, col):
    """
    Converts row-column indices to letter-number position and returns in the 
    form of a string.
    """
    row_dict = {}
    for cha, val in enumerate(LETTERS, 0):
        row_dict[cha] = val
    letter = row_dict[row]
    num = str(col + 1)
    letter_num = letter+num
    return letter_num
    
def initialize(board):
    """
    Initailizes the board. If the board is of even length, two black pieces are 
    placed diagonally right and two white pieces placed diagonally left in the 
    middle of the board. If the board is of odd length, sets up the board based 
    on that length minus one. 
    """
    size = board.length
    if size%2 == 0:
        mid = int(size/2)
        w1 = (mid, mid)
        b1 = (mid-1, mid)
        b2 = (mid, mid-1)
        w2 = (mid-1, mid-1)
        place_lst = [w1,w2,b1,b2]
    else:
        size = size - 1
        mid = int(size/2)
        w1 = (mid, mid)
        b1 = (mid-1, mid)
        b2 = (mid, mid-1)
        w2 = (mid-1, mid-1)
        place_lst = [w1,w2,b1,b2]
    for i in range(4):
        place_lst[i] = deindexify(place_lst[i][0], place_lst[i][1])
    for i in range(4):
        pos = indexify(place_lst[i])
        if i < 2:
            board.place(pos[0], pos[1], reversi.Piece("white"))
        else:
            board.place(pos[0], pos[1], reversi.Piece())

def count_pieces(board):
    """
    Counts how many black and white pieces are on the board and returns a 
    tuple of the count. In the tuple the first count is black and second count
    is white.
    """
    nums = board.length
    bp = 0 # Black piece count
    wp = 0 # White piece count
    
    # Iterates through all possible board positions and counts black and white 
    # pieces.
    for i in range(nums):
        for cha in range(nums):
            piece = board.get(i, cha)
            if piece == None:
                continue
            elif piece.is_white():
                wp += 1
            elif piece.is_black():
                bp += 1
    return (bp, wp)

def get_all_streaks(board, row, col, piece_arg):
    """
    Write something here
    """
    streaks = {'e': None, 'w': None, 'n': None, 's': None, \
               'ne': None, 'nw': None, 'se': None, 'sw': None}
    
    color = piece_arg.color()
    other_color = 'white' if color == 'black' else 'black'
    # north
    L = []
    c = col
    for r in range(row-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['n'] = sorted(L)

#    # east
    L = []
    c = col
    r = row
    for c in range(col+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['e'] = sorted(L)
 
#    # south
    L = []
    c = col
    r = row
    for r in range(row+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['s'] = sorted(L)

#    # west
    L = []
    c = col
    r = row
    for c in range(col-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['w'] = sorted(L)

#    # northeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row-1,-1,-1):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['ne'] = sorted(L)
        
#    # southeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row+1,board.length):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['se'] = sorted(L)
                
#    # southwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row+1,board.length):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['sw'] = sorted(L)
    
#    # northwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row-1,-1,-1):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['nw'] = sorted(L)
            
    return streaks

def get_all_capturing_cells(board, piece):
    """
    Creates/returns a dictionary of all the possible pieces a piece could 
    capture on every possible position of the board. The keys are the positions 
    and values are a list of all the possible captured pieces for the given 
    position.
    """
    streak_dict = {}
    nums = board.length
    
    # Iterates through all possible board positions and creates dictionary
    for i in range(nums):
        for cha in range(nums):
            key = (i, cha) # key for dictionary
            if board.is_free(i, cha):
                streaks_lst = [] # value for dictionary
                streaks = get_all_streaks(board, i, cha, piece)
                for val in streaks.values():
                    if len(val) > 0:
                        for cha in val:
                            streaks_lst.append(cha)
                        streaks_lst.sort()
                        streak_dict[key] = streaks_lst

    return streak_dict
                            

def get_hint(board, piece):
    """
    Goes through finds all potential moves and returns a list of the postions.
    The list is ordered from position with most captures to least. If two 
    postitions have equal captures, sorts by alphabetical order.
    """
    moves_lst = []
    position_lst = []
    moves_dict = get_all_capturing_cells(board, piece)
    
    # Sorts keys based on value size
    for key, val in moves_dict.items():
        val_len = len(val)
        key_pos = deindexify(key[0], key[1])
        moves_lst.append((key_pos, val_len))
    moves_lst = sorted(moves_lst, key = itemgetter(1, 0), reverse = True)
    
    # Creates a list of all positions to return
    for i in moves_lst:
        cha = i[0]
        position_lst.append(cha)
        
    return position_lst

def place_and_flip(board, row, col, piece):
    """
    Write something here
    """
    error_msg = "Can't place {:s} at '{:s}',".format(piece, deindexify(row,col))
    cap_cells = get_all_capturing_cells(board, piece)
    if row > board.length or col > board.length:
        raise ValueError#(error_msg, " invalid position. Type 'hint' to get suggestions.") #usure
    elif board.is_free(row, col) == False:
        raise ValueError#(error_msg, " already occupied. Type 'hint' to get suggestions.")
    elif (row, col) not in cap_cells:
        raise ValueError#(error_msg," it's not a capture. Type 'hint' to get suggestions.")
        
    board.place(row, col, piece)
    streaks = get_all_streaks(board, row, col, piece)
    
    for val in streaks.values():
        for i in val:
            p = board.get(i[0], i[1])
            p.flip()

def is_game_finished(board):
    """
    If board is full, or no moves are possible for either black or white, 
    returns True. Otherwise, returns False. 
    """
    if board.is_full():
        return True
    elif len(get_hint(board, reversi.Piece("white"))) == 0 and len(get_hint(board, reversi.Piece())) == 0:
        return True
    else:
        return False
            
def get_winner(board):
    """
    Gets the current winner by counting the number of pieces based on color. 
    Returns the color name with the most pieces. If color's have equal pieces, 
    returns 'draw'. 
    """
    count = count_pieces(board)
    bp = count[0]
    wp = count[1]
    
    if bp == wp:
        return "draw"
    elif bp > wp:
        return "black"
    else:
        return 'white'
    
def choose_color():
    """
    Prompts for a color. If color invaild, prints statement and loops until 
    vaild color is entered. Prints statement with each player's and oppenent's 
    colors. Returns tuple with player's and oppenent's colors.
    """
    while True:
        my_color = input("Pick a color:")
        if my_color.lower() == "white":
            opponent_color = "black"
            break
        elif my_color.lower() == "black":
            opponent_color = "white"
            break
        else:
            print("Wrong color, type only 'black' or 'white', try again.")
    print("You are '{:s}' and your opponent is '{:s}'.".format(my_color, opponent_color))
    return (my_color, opponent_color)
    
        
def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    """
    
    banner = """
     _____                         _ 
    |  __ \                       (_)
    | |__) |_____   _____ _ __ ___ _ 
    |  _  // _ \ \ / / _ \ '__/ __| |
    | | \ \  __/\ V /  __/ |  \__ \ |
    |_|  \_\___| \_/ \___|_|  |___/_|
    
    Developed by The Students Inc.
    CSE231 Spring Semester 2018
    Michigan State University
    East Lansing, MI 48824, USA.
    """

    prompt = "[{:s}'s turn] :> "
    print(banner)
   
    # Choose the color here
    (my_color, opponent_color) = choose_color()
    
    # Take a board of size 8x8
    # Prompt for board size
    size = input("Input a board size: ")
    board = reversi.Board(int(size))
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'white' else opponent_color
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get a piece according to turn
            piece = reversi.Piece(turn)

            # Get the command from user using input
            command = input(prompt.format(turn)).lower()
            
            # Now decide on different commands
            if command == 'exit':
                break
            elif command == 'hint':
                print("\tHint: " + ", ".join(get_hint(board, piece)))
            elif command == 'pass':
                hint = get_hint(board, piece)
                if len(hint) == 0:
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
                    print("\tHanded over to \'{:s}\'.".format(turn))
                else:
                    print("\tCan't hand over to opponent, you have moves," + \
                          " type \'hint\'.")
            else:
                    (row, col) = indexify(command)
                    place_and_flip(board, row, col, piece)
                    print("\t{:s} played {:s}.".format(turn, command))
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    winner = get_winner(board)
    if winner != 'draw':
        diff = abs(piece_count[0] - piece_count[1])
        print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
    else:
        print("This game ends in a draw.")
    # --- end of game play ---

def figure_1(board):
    """
    You can use this function to test your program
    """
    board.place(0,0,reversi.Piece('black'))
    board.place(0,3,reversi.Piece('black'))
    board.place(0,4,reversi.Piece('white'))
    board.place(0,5,reversi.Piece('white'))
    board.place(0,6,reversi.Piece('white'))
    board.place(1,1,reversi.Piece('white'))
    board.place(1,3,reversi.Piece('white'))
    board.place(1,5,reversi.Piece('white'))
    board.place(1,6,reversi.Piece('white'))
    board.place(1,7,reversi.Piece('white'))
    board.place(2,2,reversi.Piece('white'))
    board.place(2,3,reversi.Piece('black'))
    board.place(2,4,reversi.Piece('white'))
    board.place(2,5,reversi.Piece('white'))
    board.place(2,7,reversi.Piece('white'))
    board.place(3,0,reversi.Piece('black'))
    board.place(3,1,reversi.Piece('white'))
    board.place(3,2,reversi.Piece('white'))
    board.place(3,4,reversi.Piece('white'))
    board.place(3,5,reversi.Piece('white'))
    board.place(3,6,reversi.Piece('black'))
    board.place(3,7,reversi.Piece('black'))
    board.place(4,0,reversi.Piece('white'))
    board.place(4,2,reversi.Piece('white'))
    board.place(4,4,reversi.Piece('white'))
    board.place(5,0,reversi.Piece('black'))
    board.place(5,2,reversi.Piece('black'))
    board.place(5,3,reversi.Piece('white'))
    board.place(5,5,reversi.Piece('black'))
    board.place(6,0,reversi.Piece('black'))
    board.place(6,1,reversi.Piece('black'))
    board.place(6,3,reversi.Piece('white'))
    board.place(6,6,reversi.Piece('white'))
    board.place(7,1,reversi.Piece('black'))
    board.place(7,2,reversi.Piece('white'))
    board.place(7,3,reversi.Piece('black'))
    board.place(7,7,reversi.Piece('black'))
    
if __name__ == "__main__":
    game_play_human()
