#student name: Alexander Martinez
#student number: 10948024

import multiprocessing as mp

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    checkList = [False,False,False,False,False,False,False,False,False]
    validity = True

    # Updating check list. If each number is present, all of checkList will be true. 
    for row in range(9):
       index = puzzle[row][column] - 1
       if index <= 8 and index >= 0:
            checkList[index] = not checkList[index] 

    # Verify that all of checkList is true. 
    for index in range(9):
       if checkList[index] == False: 
            validity = False
    if(validity):
        print("Column "+str(column)+" valid")
    else: 
        print("Column "+str(column)+" is not valid")


def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    checkList = [False,False,False,False,False,False,False,False,False]
    validity = True

    # Updating check list. If each number is present, all of checkList will be true. 
    for col in range(9):
       index = puzzle[row][col] - 1
       if index <= 8 and index >= 0:
            checkList[index] = not checkList[index] 

    # Verify that all of checkList is true. 
    for index in range(9):
       if checkList[index] == False: 
           validity = False
    if(validity):
        print("Row "+str(row)+" valid")
    else: 
        print("Row "+str(row)+" is not valid")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    checkList = [False,False,False,False,False,False,False,False,False]
    validity = True
    startRow = int(subgrid/3)*3 #0-2 will be 0, 3-5 will be 3, 6-8 will be 6
    startCol = subgrid%3*3      #0,3,6 will be 0. 1,4,7 will be 3. 2,5,8 will be 6. 

    # Checks the specified 3x3 subgrid
    for row in range(startRow, startRow+3):
        for col in range(startCol, startCol+3):
            index = puzzle[row][col] - 1
            if index <= 8 and index >= 0:
                checkList[index] = not checkList[index] 
    
    # Verify that all of checkList is true. 
    for index in range(9):
       if checkList[index] == False: 
           validity = False
    if(validity):
        print("Subgrid "+str(subgrid)+" valid")
    else: 
        print("Subgrid "+str(subgrid)+" is not valid")




if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test1   #modify here for other testcases
    SIZE = 9
    
    processList = []

    columnProcess =[]
    for col in range(SIZE):  #checking all columns
        col_process = mp.Process(target=checkColumn, args=(testcase, col))
        processList.append(col_process)
        col_process.start()
 
    rowProcess =[]
    for row in range(SIZE):  #checking all rows
        row_process = mp.Process(target=checkRow, args=(testcase, row))
        processList.append(row_process)
        row_process.start()
  
    subgridProcess =[]
    for subgrid in range(SIZE):   #checking all subgrids
        subgrid_process = mp.Process(target=checkSubgrid, args=(testcase, subgrid))
        processList.append(subgrid_process)
        subgrid_process.start()

    # By using join this way, we make sure that all processes run in parallel 
    # while still preventing the main program from terminating early.
    # This uses max cores. However, things will print out of order. 
    for process in processList: 
        process.join()