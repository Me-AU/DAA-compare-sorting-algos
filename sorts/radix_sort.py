# Syed Ahsan Ullah Tanweer - 368319

# Define the counting sort algorithm which will be used as a subroutine in the radix sort algorithm.
def counting_sort(lst, place):
    # Get the size of the input list and initialize a list of zeros with the same size
    # as the input list, which will hold the sorted output.
    size = len(lst)
    output = [0] * size
    # Initialize a list of zeros to hold the count of each digit from 0 to 9.
    count = [0] * 10

    # Loop through the input list, counting the occurrence of each digit in the place value.
    for i in range(0, size):
        index = lst[i] // place # Get the digit in the current place value
        count[index % 10] += 1 # Increment the count for that digit

    # Calculate the running total of the counts for each digit.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Starting from the end of the input list, place each element into the sorted output list
    # based on its position in the running total of counts for its digit.
    i = size - 1
    while i >= 0:
        index = lst[i] // place # Get the digit in the current place value
        output[count[index % 10] - 1] = lst[i] # Place the element in the correct position in the output list
        count[index % 10] -= 1 # Decrement the count for that digit
        i -= 1

    # Copy the sorted output list back into the input list.
    for i in range(0, size):
        lst[i] = output[i]

# Define the radix sort algorithm which will sort the list by repeatedly calling the counting sort
# algorithm on each digit in the numbers in the list, from the least significant to the most significant.
def radix_sort(lst):
    max_element = max(lst) # Find the maximum element in the input list

    place = 1 # Initialize the place value to sort by to the least significant digit
    while max_element // place > 0: # Continue sorting until all digits have been sorted
        counting_sort(lst, place) # Sort the list by the current place value
        place *= 10 # Move to the next place value
