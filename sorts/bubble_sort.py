# Syed Ahsan Ullah Tanweer - 368319


# This function sorts an array using the bubble sort algorithm
def bubble_sort(lst):
    
  for i in range(len(lst)):
    swapped = False
    
    for j in range(0, len(lst) - i - 1):
        # swap lst[j] and lst[j+1] if lst[j] is greater than lst[j+1]
        if lst[j] > lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
        
            swapped = True
        
    if not swapped:
        break
