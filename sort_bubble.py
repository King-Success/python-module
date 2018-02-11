def bubble_sort(list):
    """This function implements the bubble sort algorithm, it sorts a list of elements by comparing two elements at the 
    same time in other to identify the smallest amongst them, a pointer starts at the first index and compares its 
    element with the one by its right, if the element at the right is less, the elements are swaped and then the pointer 
    moves to the next index and repeats the process. Once at the end of the list, if not perfectly sorted, the process is
    repeated until the list is sorted"""

    #Steps
    #Get a list
    #Assign a pointer to the first element/index on the list
    #Compare the element being pointed with the element to its imidiate right
    #If the element to the right is larger than the element being pointed at, swap them
    #Repeat this process for the second element, then the third, fourth.....to the last
    #Once at the end of the list, if the list isnt perfectly sorted, repeat the process over again

    for times in range(1, len(list) + 1):
        swap = False
        print times
        for index in range(0, len(list) - 1):
            if list[index + 1] < list[index]:
                swap = True
                temp = list[index]
                list[index] =list[index + 1]
                list[index + 1] = temp
        if swap == False:
            return list 
    return list


list = [7,6,5,4,3,2,1]
result = bubble_sort(list)
print result