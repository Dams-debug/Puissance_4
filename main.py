from puissance_4 import *

someone_won = False

while someone_won == False :
    column_choosed_1 = int(input("[Joueur 1] Dans quelle colonne voulez-vous placer votre jeton : "))
    to_play(player_1, column_choosed_1)
    display_board_game(board_game)
    h_alignment_player_1 = detect_horizontal_alignment(board_game, player_1)
    v_alignment_player_1 = detect_vertical_alignment(board_game, player_1)
    d_r_alignment_player_1 = detect_right_diagonal_alignment(board_game, player_1)
    d_l_alignment_player_1 = detect_left_diagonal_alignment(board_game, player_1)
    
    if h_alignment_player_1 :
        someone_won = True
        print("Le joueur 1 a gagné !")
        break
    elif v_alignment_player_1 :
        someone_won = True
        print("Le joueur 1 a gagné !")
        break
    elif d_r_alignment_player_1 :
        someone_won = True
        print("Le joueur 1 a gagné !")
        break
    elif d_l_alignment_player_1 :
        someone_won = True
        print("Le joueur 1 a gagné !")
        break

    print(" ")

    column_choosed_2 = int(input("[Joueur 2] Dans quelle colonne voulez-vous placer votre jeton : "))
    to_play(player_2, column_choosed_2)
    display_board_game(board_game)
    h_alignment_player_2 = detect_horizontal_alignment(board_game, player_2)
    v_alignment_player_2 = detect_vertical_alignment(board_game, player_2)
    d_r_alignment_player_2 = detect_right_diagonal_alignment(board_game, player_2)
    d_l_alignment_player_2 = detect_left_diagonal_alignment(board_game, player_2)
    
    if h_alignment_player_2 :
        someone_won = True
        print("Le joueur 2 a gagné !")
        break
    elif v_alignment_player_2 :
        someone_won = True
        print("Le joueur 2 a gagné !")
        break
    elif d_r_alignment_player_2 :
        someone_won = True
        print("Le joueur 2 a gagné !")
        break
    elif d_l_alignment_player_2 :
        someone_won = True
        print("Le joueur 2 a gagné !")
        break