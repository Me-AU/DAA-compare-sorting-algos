# Syed Ahsan Ullah Tanweer - 368319


# This function sorts an array using the insertion sort algorithm
def insertion_sort(lst):

    for step in range(1, len(lst)):
        key = lst[step]
        j = step - 1
        
        # move the elements of the sorted sub-list to create space for the key element
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        
        # insert the key element into the sorted sub-list
        lst[j + 1] = key
