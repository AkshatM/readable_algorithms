# recursive!
def binary_search(array, value):

    if not array:
        return False # or -1, etc. to indicate value does not exist in array

    midpoint = len(array)//2
    
    if array[midpoint] == value:
        return True # or 0, etc. to indicate value does not exist in array

    if array[midpoint] > value:
        return binary_search(array[:midpoint], value) 

    if array[midpoint] < value:
        return binary_search(array[midpoint + 1:], value) 

# iterative!
def binary_search(array, value):
    low, high = 0, len(array) - 1

    while low < high:

        midpoint = (low + high)//2
 
        if array[midpoint] > value:
            high = midpoint - 1
            continue

        if array[midpoint] < value:
            low = midpoint + 1
            continue

        if array[midpoint] == value:
            return True # or 0, etc. to indicate value does not exist in array

    if low == high and array[low] == value:
        return True # or 0, etc. to indicate value does not exist in array

    return False # or -1, etc. to indicate value does not exist in array
