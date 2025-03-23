import random

#legal moves,Need to work on bot and use a legal move system by using random choice
Player1 = 'x'
Player2 = 'o'
Bot = "b"
Empty_GRID = [[' ',' ',' '],[' ','b',' '],['b',' ',' ']]
GRID = Empty_GRID
Move_count:int = 0
winner = True

def available_moves():
    available_moves = []
    print("Available_moves:")
    for rows in range(3):
        for column in range(3):
            if GRID[rows][column] == " ":               
                available_moves.append([rows,column])
    print("Avialable moves are represented like:" + str(available_moves))
    print("")    
    return available_moves 


def increment_move():
    global Move_count
    Move_count += 1
    print("Move Count: " + str(Move_count))
    return Move_count

def display_grid():

    print("\n     1   2   3")
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
    c = int(input('Select column(1-3): '))
    c -= 1
    return r,c

def player2_input():
    print("Player2 Turn")
    r = int(input('Select row(1-3): '))
    r -= 1
    c = int(input('Select column(1-3): '))
    c -= 1
    return r,c

def bot_input_random():

    # moves = 
    bot_move = random.choice(available_moves())
    print(f"Inserted random value at {bot_move[0]+ 1},{bot_move[1] + 1}")
    return bot_move


def bot_input_inter():
    #Beter bot checks one move in the future and then sselects the move
    #Copy the current GRID to insert all the available values and have a check win condition
    moves = available_moves()
    print(f"Available moves after function:{moves}")
    # moves = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    #temporarily insert the value,check each value,if true inserts it
    move = random.choice(moves)
    for i in range(len(moves)):
        r = moves[i][0]
        c = moves[i][1]
        x = r,c
        GRID[r][c] = Bot
        win = check_win_condition(True)
        
        if GRID[r][c] == Bot: 
            GRID[r][c] = " "
        if win == True:
            print("Found winning move")
            move = r,c # winning move
            break
    
    return move
 

def insert_move(Player_type,x:int):
    r,c = x

    #Validates input and checks if the value is already taken
    if r > 2 or r < 0 or c > 2 or c < 0 or GRID[r][c] != " ":
        print("Invalid move,try again")
        if Player_type == Player1:
            player1_input()
        elif Player_type == Player2:
            player2_input
    
    elif GRID[r][c] == " ":
        GRID[r][c] = Player_type #r = list number,c = position in the list
        increment_move()
        display_grid()
    else:
        print(f"Unable to insert move Player:{Player_type},at :{r},{c}\n")
        

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
    
    if is_bot == False:
        winner_check(a,b)
    
    # check if its a draw
    if Move_count >= 9:
        print("Its a draw")
        print("Move count is:" + str(Move_count))
    
    return win

def winner_check(a:int,b:int):
    if type == "bot":
        return True
    else:
        if GRID[a][b] == Player1:
            print("Player1 Won")
        else:
            print("Player2 Won")
        playagain_prompt()

def playagain_prompt():
    global GRID,Empty_GRID,Move_count
    GRID = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    Move_count = 0
    
    choice = input("Press any key to play again:")
    if choice == "n" or choice == "N" or choice == "0":
        winner = False

# Main program flow
print("   =============")
print("    TIC TAC TOE")
print("   =============")

display_grid()
print("\nSelect mode\n 1. Player vs Player\n 2. Player vs Bot")
mode = int(input("Enter mode:"))

if mode == 2:
    print("Select Bot Type: \n 1) Easy \n 2) Intermediate")
    bot_mode = int(input("Enter bot mode:"))
    if bot_mode > 0 or bot_mode < 3:
        mode = bot_mode + 1

# mode1 is player2,m2 is random_bot,m3 is intermediate_bot
while winner:
    insert_move(Player1,player1_input())
    if mode == 1:
        insert_move(Player2,player2_input())
    elif mode == 2:
        insert_move(Bot,bot_input_random())
    else:
        insert_move(Bot,bot_input_inter())

    if Move_count >= 5:
        print("Checking Win")
        check_win_condition()
