# Syed Ahsan Ullah Tanweer - 368319

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # recursively sort the left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # merge the two halves together
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # add any remaining elements from left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # add any remaining elements from right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
