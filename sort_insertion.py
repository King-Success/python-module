def insertion_sort(list):
    """The insertion sort uses a pointer to point at an element, for each element being pointed(usually starting from 
    the second element),a comparism is carried out with the elements to its left, if the element to its left is greater
    than the element being pointed, it assumes the position of the element being pointed while the comparism continues
    until a point where the element to the left isnt greater than the one being pointed at, it is at this point that the
    element being pointerd at settles(settlement would be at the index of the last element which was found to be greater)."""

    #Steps
    #Get a list
    #Point to the element on the second index
    #Compare this element with the ones below starting from the imidiate
    #If the one imidiately below is more the element being pointed replace the element being pointed with it
    #Proceed to the next element below, if more replace again, else stop and insert the element being pointed at to the 
    #last index being shifted
    #Repeat this process for the rest of the elements accordingly until the list is perfectly sorted

    for index in range(1, len(list)):
        current_element = list[index]
        compare_index = index - 1
        if list[compare_index] > current_element:
            while compare_index >= 0 and list[compare_index] > current_element:
                list[index] = list[compare_index]
                compare_index -= 1
                index -= 1
            list[index] = current_element
    return list

list = [4,1,6,5,3,5,7,9,7,5,3,3]
result = insertion_sort(list)
print result