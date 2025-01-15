# student name: Alexander Martinez
# student number: 10948024

# A command-line 2048 game

import random

board: list[list] = []  # a 2-D list to keep the current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and prints a welcome message
    """
    # initialize the board cells with ''
    for _ in range(4):     
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)
    # add two starting 2's at random cells
    twoRandomNumbers = random.sample(range(16), 2)   # randomly choose two numbers between 0 and 15   
    # correspond each of the two random numbers to the corresponding cell
    twoRandomCells = ((twoRandomNumbers[0]//4,twoRandomNumbers[0]%4),
                      (twoRandomNumbers[1]//4,twoRandomNumbers[1]%4))
    for cell in twoRandomCells:  # put a 2 on each of the two chosen random cells
        board[cell[0]][cell[1]] = 2

    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """
    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer until a valid next move or Q (to quit) is selected
        (valid move direction: one of 'W', 'A', 'S' or 'D')
        returns the user input
    """
    print("Enter one of WASD (move direction) or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D', 'Q'): # a valid move direction or 'Q'
            break
        print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input
    return move

def addANewTwoToBoard() -> None:
    """ 
        adds a new 2 at an available randomly-selected cell of the board
    """
    emptyCells: list = []

    for row in range(4):
        for col in range(4):
            if(board[row][col] == ''):
                emptyCells.append(row*10 + col)

    newTwoLocation = random.choice(emptyCells)
    newCol = newTwoLocation % 10
    newRow = (int)(newTwoLocation / 10)
    board[newRow][newCol] = 2


def isFull() -> bool:
    """ 
        returns True if no empty cell is left, False otherwise 
    """
    for row in range(4):
        for col in range(4):
            if(board[row][col] == ''):
                return False 
    return True

def getCurrentScore() -> int:
    """ 
        calculates and returns the current score
        the score is the sum of all the numbers currently on the board
    """
    currentScore = 0
    for row in range(4):
        for col in range(4):
            if board[row][col] != '':
                currentScore += int(board[row][col])
    return currentScore

def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    """
        updates the board variable based on the move argument by sliding and merging
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """
    if move == 'W': #Iterate from top to bottom for each column 
        for col in range(4):
            for row in range(4): # shift numbers up to empty spots or combine like numbers
                #The statement below shifts to empty spots
                if board[row][col] != '' and nextEmpty(move, col) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[nextEmpty(move, col)][col] = temp
            for row in range(4):
                #The statement below combines like numbers
                if row != 3 and board[row+1][col] == board[row][col] and (board[row+1][col] and board[row][col]) != '':
                    board[row+1][col] = int(board[row+1][col])*2
                    board[row][col] = ''
            for row in range(4): # shift numbers up to empty spots or combine like numbers
                #The statement below shifts to empty spots
                if board[row][col] != '' and nextEmpty(move, col) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[nextEmpty(move, col)][col] = temp
            
    if move == 'S': #Iterate from bottom to top for each column 
        for col in range(4):
            for row in range(3, -1, -1):
                #The statement below shifts to empty spots
                if board[row][col] != '' and nextEmpty(move, col) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[nextEmpty(move, col)][col] = temp
            for row in range(3, -1, -1):
                #The statement below combines like numbers
                if row != 0 and board[row][col] == board[row-1][col] and (board[row][col] and board[row-1][col]) != '':
                    board[row-1][col] = int(board[row-1][col])*2
                    board[row][col] = ''
            for row in range(3, -1, -1):
                #The statement below shifts to empty spots
                if board[row][col] != '' and nextEmpty(move, col) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[nextEmpty(move, col)][col] = temp
    
    if move == 'A': #Iterate from left to right for each row 
        for row in range(4):
            for col in range(4):
                if board[row][col] != '' and nextEmpty(move, row) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[row][nextEmpty(move, row)] = temp
            for col in range(4):
                if col!=3 and board[row][col] == board[row][col+1] and (board[row][col] and board[row][col+1]) != '':
                    board[row][col+1] = int(board[row][col+1])*2
                    board[row][col] = ''
            for col in range(4):
                if board[row][col] != '' and nextEmpty(move, row) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[row][nextEmpty(move, row)] = temp


    if move == 'D': #Iterate from right to left for each row 
        for row in range(4):
            for col in range(3, -1, -1):
                if board[row][col] != '' and nextEmpty(move, row) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[row][nextEmpty(move, row)] = temp
            for col in range(3, -1, -1):
                if col!=0 and board[row][col-1] == board[row][col] and (board[row][col-1] and board[row][col]) != '':
                    board[row][col-1] = int(board[row][col-1])*2
                    board[row][col] = ''
            for col in range(3, -1, -1):
                if board[row][col] != '' and nextEmpty(move, row) != -1:
                    temp = board[row][col]
                    board[row][col] = ''
                    board[row][nextEmpty(move, row)] = temp


#up to two new functions allowed to be added (if needed)
#as usual, they must be documented well
#they have to be placed below this line

def nextEmpty(move: str, index: int) -> int:
    """
        Returns the next empty spot given a move and an index. 
        The index is either a row or column given the move. 
    """
    emptySpot = -1

    if move == 'W': #Bottom to top. Index is a column. 
        for row in range(3, -1, -1):
            if board[row][index] == '':
                emptySpot = row
        return emptySpot
    
    if move == 'S': #Top to bottom. Index is a column. 
        for row in range(4):
            if board[row][index] == '':
                emptySpot = row
        return emptySpot

    if move == 'A': #Right to left. Index is a row. 
        for col in range(3, -1, -1):
            if board[index][col] == '':
                emptySpot = col
        return emptySpot
    
    if move == 'D': #Left to right. Index is a row. 
        for col in range(4):
            if board[index][col] == '':
                emptySpot = col
        return emptySpot

if __name__ == "__main__":  # Use as is  
    init()
    displayGame()
    while True:  # Super-loop for the game
        print(f"Score: {getCurrentScore()}")
        userInput = promptGamerForTheNextMove()
        if(userInput == 'Q'):
            print("Exiting the game. Thanks for playing!")
            break
        updateTheBoardBasedOnTheUserMove(userInput)
        addANewTwoToBoard()
        displayGame()

        if isFull(): #game is over once all cells are taken
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break