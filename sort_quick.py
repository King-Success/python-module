def quick_sort(list):
    """This function implements the quick sort algorithm.There are many ways to implement this algorithm but the main
    principle behind it is that a pivot point is selected which determines the point at which list is going to be divided.
    This pivot point could be selected to be the first, the  middle or the last element on the list, which ever is best 
    for you for me i am gonna go with the middle element because it requires me to write lesser code than the rest.The next
    step is to compare the this middle element with all other elements on the list.Any element smaller than the middle element
    now pivot value, should be place in one of the two new list called smaller, elements larger than the pivot value should 
    be placed in the second list called larger.This process should be repeated for the two new lists simultanoeusly until
    the lists are nolonger divisible.Then at this point is where you begin to merge the join the lists together with the 
    middle elements"""

    #Steps
    #Get a list
    #Determine the middle element and assign it to a variable Pivot_element
    #Determine what and what elements are less than and greater than the pivot element
    #Place these elements accordingly into one of the two new list(smaller and larger)
    #For each of these list, repeat this process until the resulting lists are nolonger divislble
    #At this point, join the two now indivisible lists with the pivot element with smaller at the left, pivot at the 
    #middle and larger at the right
    #Continue this process until a well sorted list containing all the elements in the first list is created

    if len(list) > 1:
        pivot_value = len(list)/2
        index = 0
        smaller = []
        larger = []

        while index < len(list):
            if index != pivot_value:
                if list[index] <= list[pivot_value]:
                    smaller.append(list[index])
                else:
                    larger.append(list[index])
            index += 1
        
        quick_sort(smaller)
        quick_sort(larger)

        list[:] = smaller + [list[pivot_value]] + larger
        return list

list = [7,4,2,5,8,9,3,2]
result = quick_sort(list)
print result