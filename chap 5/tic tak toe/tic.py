"""  

core logic is make array where the solutions are there for example: 
2d array = [ [ ] , [ ] , [ ] ] so on
cross = true ,
Horizontalline = true,
verticalLine = true

"""

# create gameBoard
print("gameBoard ! ")
# one liner for  " " make look for emplty string in array format like 012345678
# gameBoard = [ ["" , " " , " "], ["" , " " , " "] ,["" , " " , " "] ] goes like this manually
# for i in range(9): <-just replay with "gameBoard"
#     print(i)
gameBoard = [' ' for _ in range(9)]

"""
0 1 2 
3 4 5
6 7 8
 
"""
solution_pt = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # verti
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # hori
        [0, 4, 8], [2, 4, 6]              # crosss
    ]


# soultion pattern check
def soultions(gameBoard, player):

    for pt in solution_pt:
        print(pt)
        if all(gameBoard[i] == player for i in pt):
            print(pt)
            return 1
    return 0

# if string is empty then draw
def check_draw(gameBoard):
    return ' ' not in gameBoard

def display_gameBoard(gameBoard):
    
    print(f"{gameBoard[0]}|{gameBoard[1]}|{gameBoard[2]}")
    print("-----")
    print(f"{gameBoard[3]}|{gameBoard[4]}|{gameBoard[5]}")
    print("-----")
    print(f"{gameBoard[6]}|{gameBoard[7]}|{gameBoard[8]}")

def turn(player, gameBoard):
    while True:
        try:
            pos = int(input(f"{player}'s turn. Choose a pos (0-8): "))
            if 0 <= pos <= 8 and gameBoard[pos] == ' ':
                gameBoard[pos] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")



# call all function's
def play_game():
    current_player = 'x'
    game_over = False 

    while not game_over:
        display_gameBoard(gameBoard)
        turn(current_player, gameBoard)

        if not game_over:

            if soultions(gameBoard, current_player):
                display_gameBoard(gameBoard)
                print(f"{current_player} wins!")
                game_over = True
            elif check_draw(gameBoard):
                display_gameBoard(gameBoard)
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'x' else 'x'

# Start the game
play_game()


