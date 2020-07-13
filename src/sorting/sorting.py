# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a_index = 0
    b_index = 0

    for cur_idx in range(elements):
        if a_index == len(arrA):
            merged_arr[cur_idx] = arrB[b_index]
            b_index += 1
        elif b_index == len(arrB):
            merged_arr[cur_idx] = arrA[a_index]
            a_index += 1
        elif arrA[a_index] <= arrB[b_index]:
            merged_arr[cur_idx] = arrA[a_index]
            a_index += 1
        else:
            merged_arr[cur_idx] = arrB[b_index]
            b_index += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        mid_index = len(arr) // 2
        return merge(merge_sort(arr[0:mid_index]), merge_sort(arr[mid_index:]))
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr1)
arr1 = merge_sort(arr1)
print(arr1)