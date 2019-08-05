def mergesort(array):

    def merge(A, B):
        """ A, B are both arrays """
        
        if A == []:
            return B

        if B == []:
            return A

        if A[0] > B[0]:
            return [A[0]] + merge(A[1:], B)

        if B[0] > A[0]:
            return [B[0]] + merge(A, B[1:])
    
    if len(array) == 1:
        return array
    
    midpoint = floor(len(array)/2)
    return merge(mergesort(array[:midpoint]), mergesort(array[midpoint:]))

