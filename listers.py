""" 1)possible bug:  changed code to also test for list of empty lists [[],[],.....] instead of 
    just one big empty list [] now it tests for both. Use a temp variable = 0 and a for loop to 
    go thru listOfLists and if length of any list is greater than 0 (not empty) then store new length in listlength.
    then you can test and if all lists are empty listlength will still be = 0


    2)conceptaul error: the following error is in how bigNumList is used but it does not effect the final answer. 
    the program is storing the wrong thing in bigNumList when it encounters a empty list mixed in with nonemtpy lists.
    I fixed it by storing None in bigNumList whenever I find an empty list.  Run my tests and you will see the problem
    in bigNumList caused by listOfLists that has empty lists mixed in with nonempty. The biggest number in an
    empty list should be nothing and not some number (zero is still a number, None is a better representation).
    uncomment lines that have # at the start (31,36,37,41) and run again and you will see the fix in bigNumList. 
    I used None type to represent the lists that were empty in bigNumList and when you look thru bigNumList 
    now for the largest its position will correspond to the position of the list it came from 
    and if it is None type then the test is just skipped.
"""

def  listyMax(listOfLists):
    
    listlength = 0
    for lists in listOfLists:
        length = len(lists)
        if length > listlength:
            listlength = length
    if listlength == 0:      
        print("Error: no lists")
    else:                   
        biggest_num = 0
        bigNumList = []
        for myList in listOfLists:
            #if len(myList) != 0:
                for number in myList:
                    if number >= biggest_num:
                        biggest_num = number
                bigNumList.append( biggest_num )
                biggest_num = 0
            #else:
                #bigNumList.append( None )
        biggest_num = 0
        print("listOfLists is: {}  bigNumList: {} \n".format(listOfLists,bigNumList))
        for nums in bigNumList:
            #if nums != None:
                if nums >= biggest_num:
                    biggest_num = nums
        
        print("biggest_num: {} and biggest list: {} \n\n\n".format(biggest_num,listOfLists[bigNumList.index(biggest_num)]))
     

lists = [[1,2,3],[4,5,6],[7,8,9]]
listyMax(lists)

lists = [[3,2,1],[],[7,9,8]]
listyMax(lists)

lists = [[],[3,1,2],[10,4,8],[9,3]]
listyMax(lists)

lists = [[],[],[]]
listyMax(lists)

lists = []
listyMax(lists)

lists = [[],[1,2],[],[4,5,6],[9],[]]
listyMax(lists)
