#student name: Alexander Martinez 
#student number: 10948024

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    if(firstHalf):
        endIndex = int(len(testcase)/2)

        # Adding testcase first half to list 
        for i in range(endIndex):
            sortedFirstHalf.append(testcase[i])

        # Sorting first half 
        for i in range(endIndex):
            for j in range(0, endIndex-i-1):
                if sortedFirstHalf[j] > sortedFirstHalf[j+1]:  # Swap if the element found is greater
                    sortedFirstHalf[j], sortedFirstHalf[j+1] = sortedFirstHalf[j+1], sortedFirstHalf[j]
    else:
        startIndex = int(len(testcase)/2)
        endIndex = len(testcase)

        # Adding the second half of the testcase to sortedSecondHalf
        for i in range(startIndex, endIndex):
            sortedSecondHalf.append(testcase[i])

        # Sorting the second half using bubble sort
        for i in range(len(sortedSecondHalf)):         
            for j in range(len(sortedSecondHalf) - i - 1):
                if sortedSecondHalf[j] > sortedSecondHalf[j + 1]:  # Swap if the element found is greater
                    sortedSecondHalf[j], sortedSecondHalf[j + 1] = sortedSecondHalf[j + 1], sortedSecondHalf[j]

        

def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    i = 0 
    j = 0

    # Merge elements from both halves
    while i < len(sortedFirstHalf) and j < len(sortedSecondHalf):
        if sortedFirstHalf[i] < sortedSecondHalf[j]:
            SortedFullList.append(sortedFirstHalf[i])
            i += 1
        else:
            SortedFullList.append(sortedSecondHalf[j])
            j += 1

    # Add any remaining elements from first_half
    while i < len(sortedFirstHalf):
        SortedFullList.append(sortedFirstHalf[i])
        i += 1

    # Add any remaining elements from second_half
    while j < len(sortedSecondHalf):
        SortedFullList.append(sortedSecondHalf[j])
        j += 1
    

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2, 5, 5, 66, -5, -20]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    first = threading.Thread(target=sortingWorker, args=(True,))
    second = threading.Thread(target=sortingWorker, args=(False,))
    full = threading.Thread(target=mergingWorker)

    # Starting and joining the 2 half sorting threads
    first.start()
    second.start()
    first.join()
    second.join()

    # Starting and joining the merging thread
    full.start()
    full.join()



    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)