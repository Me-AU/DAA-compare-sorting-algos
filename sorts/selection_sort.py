# Syed Ahsan Ullah Tanweer - 368319

def selection_sort(lst):
    size = len(lst)

    # traverse through all array elements
    for step in range(size):
        min_idx = step

        # find the minimum element in remaining unsorted array
        for i in range(step + 1, size):
            if lst[i] < lst[min_idx]:
                min_idx = i

        # swap the found minimum element with the first element
        lst[step], lst[min_idx] = lst[min_idx], lst[step]
