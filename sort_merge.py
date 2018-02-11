def merge_sort(list):
    """This function implements the merge sort algorithm.Here, a list is sorted by first breaking it down into its
    smallest units, once broken, a merge action is carried out by comparing this units and then placing the smallest
    where it belongs, that means that for the first and second elements, a new list is created where the smallest
    amongst the two takes the first index while the next index is taken by the second element. This newly created
    list is subsequently merged with the other newly created list(This process happens homogenously, creating two lists 
    at the same time). As this process continues, the elements in each list gets larger. This process is continued until
    a final list is created containing all the elements in sorted order"""

    #Steps
    #Get a list
    #Divide the list into two parts
    #Divide the two parts into two parts(totaling 4), continue until the lists becomes indivisible
    #Begin by merging the first two elements i.e create a new list and then put the smallest amongst the two in the fist
    #index creating a new list of 2 elements
    #With this new lists, merge the two thus creating another list with four elements
    #Repeat this process until a single final list is created containing all the elements in the initial list by 
    #this time in a sorted way.

    if len(list) > 1:
        middle = len(list)/2
        list_a = list[:middle]
        list_b = list[middle:]

        merge_sort(list_a)
        merge_sort(list_b)

        i = 0
        j = 0
        k = 0

        while i < len(list_a) and j < len(list_b):
            if list_a[i] <= list_b[j]:
                list[k] = list_a[i]
                i += 1
                k += 1
            else:
                list[k] = list_b[j]
                j += 1
                k += 1
        
        while i < len(list_a):
            list[k] = list_a[i]
            i += 1
            k += 1

        while j < len(list_b):
            list[k] = list_b[j]
            j += 1
            k += 1

        return list
    else:
        return list

list = []
result = merge_sort(list)
print result