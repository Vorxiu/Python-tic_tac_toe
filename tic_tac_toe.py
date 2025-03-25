import random

Player1 = 'x'
Player2 = 'o'
Bot = "b"
Move_count:int = 0
GRID = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
winner = True

def available_moves():
    available_moves = []
    for rows in range(3):
        for column in range(3):
            if GRID[rows][column] == " ":                
                available_moves.append([rows,column])
    return available_moves

def display_grid():

    # print("\n     1   2   3")
    print("\n     a   b   c")    
    print("    ___________  ")
    print(f" 1 | {GRID[0][0]} | {GRID[0][1]} | {GRID[0][2]} |")
    print("   |–––|–––|–––|")
    print(f" 2 | {GRID[1][0]} | {GRID[1][1]} | {GRID[1][2]} |")
    print("   |–––|–––|–––|")    
    print(f" 3 | {GRID[2][0]} | {GRID[2][1]} | {GRID[2][2]} |")
    print(f"    ‾‾‾‾‾‾‾‾‾‾‾ ") 
    
    # for i in GRID:
    #     print(i)

def player1_input():
    print("Player1 Turn")
    r = int(input('Select row(1-3): '))
    r -= 1
    c = input('Select column(a-c): ')
    # c -= 1
    if c == "a":
        c = 0
    elif c == "b":
        c = 1
    elif c == "c":
        c = 2
    else:
        int(c)
        c -= 1
    int(c)
    return r,c

def player2_input():
    print("Player2 Turn")
    r = int(input('Select row(1-3): '))
    r -= 1
    c = int(input('Select column(a-c): '))
    # c -= 1
    if c == "a":
        c = 0
    elif c == "b":
        c = 1
    elif c == "c":
        c = 2
    else:
        int(c)
        c -= 1
    int(c)
    return r,c

def bot_input_random(bot_move_value):

    moves = available_moves()
    print(f"Available moves after function:{moves}")
    move = random.choice(moves)
    #checks winning move
    for i in range(len(moves)):
        r = moves[i][0]
        c = moves[i][1]
        GRID[r][c] = bot_move_value
        win = check_win_condition(True)
        
        if GRID[r][c] == bot_move_value: 
            GRID[r][c] = " "
        if win == True:
            # print("Found winning move")
            move = r,c # winning move
            break
    
    return move

def bot_input_inter(Other_player_move_value,bot_move_value):

    moves = available_moves()
    # print(f"Available moves after function:{moves}")
    
    random_move = random.choice(moves)
    #checks winning move
    for i in range(len(moves)):
        r = moves[i][0]
        c = moves[i][1]
        GRID[r][c] = bot_move_value
        win = check_win_condition(True)
        
        if GRID[r][c] == bot_move_value: 
            GRID[r][c] = " "
        if win == True:
            # print("Found winning move")
            winning_move = r, c # winning move
            return winning_move
    
    #checks losing move
    for j in range(len(moves)):
        r1 = moves[j][0]
        c1 = moves[j][1]
        GRID[r1][c1] = Other_player_move_value
        win1 = check_win_condition(True)
        if GRID[r1][c1] == Other_player_move_value: 
            GRID[r1][c1] = " " 
        if win1 == True:
            # print("Found blocking move") 
            losing_move = r1,c1 # losing move
            return losing_move
            #If the center is empty returns its position
    #priritizes the center abd corner moves
    if GRID[1][1] == " ":
        return 1,1
    if Move_count > 1:
        #If there is an emoty corner return its psotion
        coner_moves = [[0,0],[0,2],[2,0],[2,2]]
        if coner_moves in moves:
            return random.choice(coner_moves)
    return random_move

def bot_input_advanc(Other_player_move_value,bot_move_value):
    #The type of value used by bot or player eg. x or o
    moves = available_moves()
    random_move = random.choice(moves)
    #checks winning move
    for i in range(len(moves)):
        r = moves[i][0]
        c = moves[i][1]
        GRID[r][c] = bot_move_value
        win = check_win_condition(True)
        
        if GRID[r][c] == bot_move_value: 
            GRID[r][c] = " "
        if win == True:
            # print("Found winning move")
            winning_move = r, c # winning move
            return winning_move
    
    #checks losing move
    for j in range(len(moves)):
        r1 = moves[j][0]
        c1 = moves[j][1]
        GRID[r1][c1] = Other_player_move_value
        win1 = check_win_condition(True)
        if GRID[r1][c1] == Other_player_move_value: 
            GRID[r1][c1] = " " 
        if win1 == True:
            # print("Found blocking move") 
            losing_move = r1,c1 # losing move
            return losing_move
    
    #checks two moves ahead in the future
    if Move_count > 2:
        for a in range(len(moves)):
            x1 = moves[a][0]
            y1 = moves[a][1]
            GRID[x1][y1] = bot_move_value
            future_moves = available_moves()
            
            for b in range(len(future_moves)):
                x2 = future_moves[b][0]
                y2 = future_moves[b][1]
                GRID[x2][y2] = bot_move_value
                win1 = check_win_condition(True)
                if GRID[x2][y2] == bot_move_value:
                    GRID[x2][y2] = " "
                if win1 == True:
                    break
            
            if GRID[x1][y1] == bot_move_value:
                GRID[x1][y1] = " "
            if win1 == True:
                # print("Found W move")
                w_move = x1,y1
                return w_move #The move that may lead to a win
    
    #If the center is empty returns its position
    if GRID[1][1] == " ":
        return 1,1
    if Move_count > 1:
        #If there is an emoty corner return its psotion
        coner_moves = [[0,0],[0,2],[2,0],[2,2]]
        if coner_moves in moves:
            return random.choice(coner_moves)
    # for rw,col in coner_moves:
    #     if GRID[rw][col] == " ":
    #         return rw,col
    
    return random_move
    
def insert_move(Player_type,x:int):
    global Move_count
    r,c = x

    #Validates input and checks if the value is already taken
    if r > 2 or r < 0 or c > 2 or c < 0 or GRID[r][c] != " ":
        print("Invalid move,try again")
        if Player_type == Player1:
            p1 = player1_input()
            insert_move(Player1,p1)
        
        elif Player_type == Player2:
            p2 = player2_input()
            insert_move(Player2,p2)

    
    elif GRID[r][c] == " ":
        GRID[r][c] = Player_type #r = list number,c = position in the list
        Move_count += 1
        return True
    else:
        print(f"Unable to insert move Player:{Player_type},at :{r},{c}\n")
        return False

def check_win_condition(is_bot):
    win = False
    #Check diagonally
    if GRID[0][0] == GRID[1][1] == GRID[2][2] and GRID[0][0] != " ":
        # winner_check(0,0)
        a,b = 0,0
        win = True            
    elif GRID[0][2] == GRID[1][1] == GRID[2][0] and GRID[0][2] != " ":
        # winner_check(0,2)
        a,b = 0,2
        win = True
    
    #Checks each row for matching row
    for i in range(0,3):
        if GRID[i][0] == GRID[i][1] == GRID[i][2] and GRID[i][0] != " ":
            # winner_check(i,0)
            a,b = i,0
            win = True
            break

    #Checks each column for matching column
    for i in range(0,3):
        if GRID[0][i] == GRID[1][i] == GRID[2][i] and GRID[0][i] != " ":
            # winner_check(0,i)
            a,b = 0,i
            win = True
            break
    #if there is a winner then prints the relevant message
    if is_bot == False and win == True:
        winner_check(a,b)
    
    return win

def winner_check(a:int,b:int):
    global b_w1,b_w2
    if GRID[a][b] == Player1:
        print("Player1 Won 🎉")

    else:
        print("Player2 Won 🎉")

    playagain_prompt()

def playagain_prompt():
    global GRID,Move_count,winner
    GRID = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    Move_count = 0
    if bot_mode == 0:
        display_grid()
        main()
    else:
        choice = input("Press any key to play again:")
        if choice == "n" or choice == "N" or choice == "0":
            winner = False
        else:
            display_grid()
            main()

def main():
    global winner
    while winner:
        #Player 1 input
        insert_move(Player1,player1_input())
        # insert_move(Player1,bot_input_inter(Bot,Player1)) #Bot input x
        display_grid()
        
        #Checks the win condition
        if Move_count >= 5 and Move_count <= 9:
            # print("Checking Win")
            if check_win_condition(False):
                if winner == False:
                    break

        if Move_count <= 8: 
            #Player 2 input
            if mode == 1:
                # insert_move(Player2,player2_input())
                insert_move(Bot,bot_input_inter(Player1,Bot))
            elif mode == 2:
                insert_move(Bot,bot_input_random(Bot))
            elif mode == 3:
                insert_move(Bot,bot_input_inter(Player1,Bot))
            else:
                insert_move(Bot,bot_input_advanc(Player1,Bot))
            display_grid()
        
        #Checks the win condition
        if Move_count >= 5 and Move_count <= 9:
            # print("Checking Win")
            if check_win_condition(False):
                if winner == False:
                    break
        # check if its a draw
        if Move_count >= 9:
            print("Its a draw 🤝")
            playagain_prompt()
    if bot_mode == 0:
        print(f"Bot:\n Player1: {b_w1} Player2: {b_w2}")
    print("Exiting Game")

# Main program flow
print("   =============")
print("    TIC TAC TOE")
print("   =============")
display_grid()

# mode1 is player2,m2 is random_bot,m3 is intermediate_bot,4 is advanced_bot,
print("\nSelect mode\n 1. Player vs Player\n 2. Player vs Bot\n 3. Bot vs Player")
mode = int(input("Enter mode: "))
if mode == 3:
    mode = 1

if mode == 2:
    print("Select Bot Type: \n 1) Easy \n 2) Intermediate \n 3) Casual bot")
    bot_mode = int(input("Enter bot mode: "))
    
    if bot_mode == 1  or bot_mode == 2 or bot_mode == 3:
        mode = bot_mode + 1

display_grid()
main()