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
    
    testcase = test1  # or test2
    SIZE = 9

    column_processes = []
    for col in range(SIZE): #checking all columns
        p = mp.Process(target=checkColumn, args=(testcase, col))
        p.start()
        column_processes.append(p)
    # Runs all column processes in parallel and waits for them to finish. 
    for p in column_processes:
        p.join()  

    row_processes = [] #checking all rows 
    for row in range(SIZE):
        p = mp.Process(target=checkRow, args=(testcase, row))
        p.start()
        row_processes.append(p)
    # Runs all row processes in parallel and waits for them to finish. 
    for p in row_processes:
        p.join()  

    subgrid_processes = [] #checking all subgrids
    for subgrid in range(SIZE):
        p = mp.Process(target=checkSubgrid, args=(testcase, subgrid))
        p.start()
        subgrid_processes.append(p)
    # Runs all subgrid processes in parallel and waits for them to finish. 
    for p in subgrid_processes:
        p.join()  