def binary_search(list, item):
    """This function implements a binary search algorithm.This algorithm searches for an item by picking the middle 
    element from the list and comparing it to the item being searched for.If they are exactly the same, the program
    stops and returns the element, if they are not, the program decides whether the element belongs to the left side
    (i.e if it is less than the middle elements) or not. If it does, it discards the second half and vice versa.
    This process is repeated until the element is found. If the element doesnt exist, the program stops once it 
    reaches the last element. This algorithm only applies to sorted list as you might have rightly guessed"""


    #Steps
    #Get a list
    #Point at the middle element of the list
    #If the middle element is equivalent to the one being searched for stop
    #Else determine if the element belong to the left or right side of the list
    #Depending on where it belongs, discard the other half and continue this process until you find the element
    #Once at the last element and if it doesnt match the item being searched for stop and return False
    if len(list) > 1:
        middle = len(list)/2
        if list[middle] == item:
            print "Item Found"
        if item < list[middle]:
            list = list[:middle]
        else:
            list = list[middle + 1:]
        
        binary_search(list, item)
    else:
        if item == list[0]:
             print "Item Found"
        else:
            print "Item does not exist"

list = [0,2,3,4,5,6,7,8,9]
result = binary_search(list, 0)
print result


