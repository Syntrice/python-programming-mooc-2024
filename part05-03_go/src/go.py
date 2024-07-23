# Write your solution here
 
def who_won(game_board: list):
    
    player_1 = 0
    player_2 = 0
    
    for row in game_board:
        for cell in row:
            if cell == 1: player_1 += 1
            elif cell == 2: player_2 += 1
            
    if player_1 > player_2:
        return 1
    elif player_2 > player_1:
        return 2
    else:
        return 0
    