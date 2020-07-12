# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    rtn_index = -1

    if len(arr) <= 0:
        return rtn_index

    if start > end:
        return rtn_index

    cur_index = ((end - start) // 2) + start
    if arr[cur_index] == target:
        rtn_index = cur_index
    elif cur_index == end:
        rtn_index - 1
    elif arr[cur_index] < target:
        rtn_index = binary_search(arr, target, cur_index+1, end)
    elif arr[cur_index] > target:
        rtn_index = binary_search(arr, target, start, cur_index-1)

    return rtn_index


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here