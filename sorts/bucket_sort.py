# Syed Ahsan Ullah Tanweer - 368319

def bucket_sort(x):
    arr = []
    num_slots = 10

    # initialize empty buckets
    for i in range(num_slots):
        arr.append([])

    # put elements into their respective buckets
    for j in x:
        index_b = int(num_slots * j)
        arr[index_b].append(j)

    # sort the elements in each bucket
    for i in range(num_slots):
        arr[i] = sorted(arr[i])

    # concatenate the sorted buckets
    k = 0
    for i in range(num_slots):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x
