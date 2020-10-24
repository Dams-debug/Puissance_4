#1 ========
board_game = [
    ['_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_'],
    ['_','_','_','_','_','_','_'],
]

player_1 = 'O'
player_2 = 'X'

def display_board_game(board) :
    for i in range(0, len(board_game)) :
        print(board[i])
print("======== Début de la partie ========")
display_board_game(board_game)
print("====================================")

# =========

#2 ========

def count_empty_space(board) :
    empty_space_list = []
    for i in range(0,len(board) + 1) :
        column = []
        for j in range(0,len(board)) :
            if board[j][i] == '_' :
                column.append(board[j][i])
        empty_space_list.append(column)
        column = []
    return empty_space_list

''' 
print(empty_space_list[0:], sep="\n")

for i in range(0, len(empty_space_list)) :
    if len(empty_space_list[i]) < 6 :
        print("La colonne ", i + 1, " contient un ou plusieurs jetons.")
    else :
        print("La colonne ", i + 1, " est vide.")
'''

# =========

#3 ========

def to_play(player, column) :
    empty_spaces = count_empty_space(board_game)
    nb_of_slots = len(empty_spaces[column])
    if nb_of_slots <= 6 :
        board_game[nb_of_slots - 1][column] = player

# =========

#4 ========

def detect_horizontal_alignment(board_game, player) :
    for i in range(0,len(board_game)) :
        for j in range(0,4) : 
            nb = 0
            for k in range(0,4) :
                if board_game[i][k+j] == player :
                    nb = nb+1
            if nb == 4:
                return  True
    return False

def detect_vertical_alignment(board_game, player) :
    for j in range(0,len(board_game[0])) :
        for i in range(0,3) : 
            nb = 0
            for k in range(0,4) :
                if board_game[k+i][j] == player:
                    nb = nb+1
            if nb == 4:
                return  True
    return False

def detect_right_diagonal_alignment(board_game, player) :
    for i in range(0,3) :
        for j in range(0, 4) : 
            nb = 0
            for k in range(0,4) :
                if board_game[i+k][j+k] == player :
                    nb = nb+1
            if nb == 4:
                return  True
    return False

def left_diagonal_alignement(board_game, row, column, player) :
    nb = 0
    for k in range(0,4) :
        if board_game[row+k][column-k] == player :
            nb = nb+1
    return nb == 4
    
def detect_left_diagonal_alignment(board_game, player) :
    for i in range(0,3) :
        for j in range(3,7) :
            if left_diagonal_alignement(board_game, i, j, player) :
                return True
    return False

# =========