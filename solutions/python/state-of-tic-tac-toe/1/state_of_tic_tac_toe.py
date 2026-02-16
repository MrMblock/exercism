def gamestate(board):
    length = 0
    for i in board:
        length += len(i.strip())

    if are_rules_respected(board):
        message = are_rules_respected(board)
        raise ValueError(message)
    
    if is_win(board):
        return "win"
    else:
        if length == 9:
            return "draw"
        else:
            return "ongoing"

    return False
    

def is_win(board):
    # case row
    for i in board:
        if "XXX" in i or "OOO" in i:
            return True
            
    # case column
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and not is_whitespace(board[1][i]):
            return True

    # case diagonal
    if board[0][0] == board[1][1] and board[2][2] == board[1][1] and not is_whitespace(board[1][1]):  
            return True
    elif board[0][2] == board[1][1] and board[2][0] == board[1][1] and not is_whitespace(board[1][1] ): 
            return True
        
    return False


def is_whitespace(text):
    if text == " ":
        return True
    return False

def are_rules_respected(board):
    demolisher = ""
    x_counter = 0
    o_counter = 0
    
    for i in board:
        demolisher += i
 
    for i in demolisher:
        if i == "X":
            x_counter += 1
        elif i == "O":
            o_counter += 1

    # case X went twice
    if x_counter == 2 and o_counter == 0:
        return "Wrong turn order: X went twice"

    # case O started
    if x_counter == 1 and o_counter == 2:
        return "Wrong turn order: O started"

    # case X won and o kept playing*
    if demolisher.strip() == "XXXOOO":
        return "Impossible board: game should have ended after the game was won"

    # case both players kept playing after a win
    if demolisher.strip() == "XXXOOOXOX":
        return "Impossible board: game should have ended after the game was won"

    return False