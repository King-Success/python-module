def selection_sort(list):
    """This sort function sorts a list of elements N by picking each element and comparing them with the rest of the
    elements on the list in an attempt to find the smallest element each time. when it does, it 
    places the smallest element on its supposed index on a sorted list while replacing its previous possition with 
    the element on its current index. it has a Big O of N squared. This algorithm does require a new list"""

    #Steps
    #Get a list
    #for each element, assign it to a variable smallest
    #loop through the remaining elements till the end
    #If you see an element less than the current smallest ,assign that element to smallest then replace smallest with the previous smallest
    #Continue until the end of the list repeating this process
    #At the end of the list the element on the smallest variable should be placed in the right index if its not equal to the current element
    #Repeat this process until the list is perfectly sorted

    for index in range(0, len(list) - 1):
        smallest = list[index]
        for j in range(index + 1, len(list)):
            if list[j] < smallest:
                smallest = list[j]
                replace_id = j
        if smallest != list[index]:
            temp = list[index]
            list[index] = smallest
            list[replace_id] = temp 
    return list

list = [7,6,5,4,3,2,3,2,1]
result = selection_sort(list)
print result