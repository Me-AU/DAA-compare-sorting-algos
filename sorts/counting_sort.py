# Syed Ahsan Ullah Tanweer - 368319


# This function sorts an array using the counting sort algorithm
def counting_sort(arr):
    size = len(arr)
    output = [0] * size

    count = [0] * 10

    # count the frequency of each element in the array
    for i in range(0, size):
        count[arr[i]] += 1

    # modify the count array to store the actual position of each element in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # fill the output array with the elements of the input array in the order determined by the count array
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # copy the output array back to the input array
    for i in range(0, size):
        arr[i] = output[i]
