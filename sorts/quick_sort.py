# Syed Ahsan Ullah Tanweer - 368319

# This function is used by the quick_sort function to partition the array 
# around a pivot and returns the partition index
def partition(lst, low, high):
    pivot = lst[high]

    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i = i + 1

            # swap lst[i] and lst[j]
            (lst[i], lst[j]) = (lst[j], lst[i])

    # swap lst[i+1] and lst[high]
    (lst[i + 1], lst[high]) = (lst[high], lst[i + 1])

    return i + 1

# This function is called by the quick_sort function recursively to sort the array
def quick_sort_aux(lst, low, high):
    if low < high:

        # partition the array around a pivot
        pi = partition(lst, low, high)

        # sort the left sub-array
        quick_sort_aux(lst, low, pi - 1)

        # sort the right sub-array
        quick_sort_aux(lst, pi + 1, high)

# This function sorts an array using the quick sort algorithm
def quick_sort(lst):
    quick_sort_aux(lst, 0, len(lst)-1)
