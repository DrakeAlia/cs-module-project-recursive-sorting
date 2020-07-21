# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(lefthalf, righthalf):
    merged_array = lefthalf + righthalf
    i = 0
    j = 0
    k = 0
    # loop if starting index is less than the length of the array
    while i < len(lefthalf) and j < len(righthalf): 
        # If the left half element is at the given index is less than or equal to the right half element at the given index
        if lefthalf[i] <= righthalf[j]: 
            # Take the given index in the merged array and set it to the element of the left half given index
            merged_array[k]=lefthalf[i] 
            # Increase the position on the left by 1
            i = i + 1 
            # If the left half element at the given index is greater than the right half element at the given index
        else:
            # Take the given index in the merged array and set it to the element of the right half given index
            merged_array[k]=righthalf[j] 
            # Increase the position on the right by 1
            j = j + 1 
        # Increase the position on the merged_array by 1
        k = k + 1 

    # loop if starting index is less than the length of the left array
    while i < len(lefthalf): 
        # Take the given index in the merged array and set it to the element of the left half given index
        merged_array[k]=lefthalf[i] 
        # Increase the position on the left by 1
        i = i + 1 
        # Increase the position on the merged_array by 1
        k = k + 1 

# loop if starting index is less than the length of the right array
    while j < len(righthalf): 
        # Take the given index in the merged array and set it to the element of the right half given index
        merged_array[k]=righthalf[j] 
        # Increase the position on the right by 1
        j = j + 1 
        # Increase the position on the merged_array by 1
        k = k + 1 
    print(f"merged array: {merged_array}")
    return merged_array

# TO-DO: Implement the Merge Sort function below recursively
def merge_sort(arr):
    # Make sure we have elements in our list
    if len(arr) > 1: 
        # Grab the mid point by taking the length and diving by 2
        mid = len(arr) // 2 
        # Declare a left side array, all the elements up to the mid point
        left = arr[:mid] 
        # Declare a right side array, all the elements from the mid point and beyond
        right = arr[mid:] 

        if len(left) > 1:
            # recursively call merge_sort()
            left = merge_sort(left)
        if len(right) > 1:
            # recursively call merge_sort() 
            right = merge_sort(right) 
        # merge sorted pieces
        arr = merge(left, right) 
    print(f"arr: {arr}")
    return arr

merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])

# STRETCH: implement the recursive logic for merge sort in a way that doesn't utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
        # pass


# def merge_sort_in_place(arr, l, r):
#     # Your code here
        # pass