##Elise Harper Tic Tac Toe Board##

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')

    return((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or #Check for winner across top
           (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or #Check for winner across the middle
           (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or #Check for winner across bottom
           (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or #Check for winner in left hand column
           (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or #Check for winner in middle column
           (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or #Check for winner in right hand column
           (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or #Check for winner diagonally
           (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player)) #Check for winner other diagonal direction
             
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer  #Starting player picks where they want to put the first X
    for i in range(9): #There are 9 spaces so this starts a loop that will run for each space
        printBoard(board) #This prints the board after each turn
        print('Turn for ' + turn + '. Move on which space?') #This asks each player where on the board they want to put their X or O
        move = input() #This takes whatever the user enters and stores it in the variable 'move'
        board[move] = turn  #This puts the users input on the actual board
        if( checkWinner(board, 'X') ):  #This starts a loop that checks if the X has won the game
            print('X wins!') #What the user sees if X has won the game
            break  #Breaks the loop
        elif ( checkWinner(board, 'O') ):  #This starts a loop that checks if O has won the game
            print('O wins!')  #What the user sees if O has won the game
            break    #Breaks the loop
    
        if turn == 'X':   #This changes turns from X to O
            turn = 'O'
        else:             #Switches back from O to X
            turn = 'X'
        
    printBoard(board)   #The command that prints the board and makes the program start running
    
