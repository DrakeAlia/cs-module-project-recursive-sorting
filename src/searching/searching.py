# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, low, high):
    # Your code here
    # loop if high is greater than or equal to low
    if high >= low:
        #  declare a mid point 
        mid = (high + low) // 2
        # If element is greater than mid, then it's in the left subarray
        if arr[mid] > target:
            #  recurse towards the base case
            return binary_search(arr, target, low, mid -1)
            # If elemnt is less than mid, then it's in the right subarray
        elif arr[mid] < target:
            # recurse towards base case
            return binary_search(arr, target, mid + 1, high)
            # If element is the target 
        elif arr[mid] == target:
            # Return element
            return mid
    # Target was not in the list
    return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
