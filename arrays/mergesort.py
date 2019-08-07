def mergesort(array):

    def merge(A, B):
        """ A, B are both arrays """
        
        if A == []:
            return B

        if B == []:
            return A

        first_element_A, first_element_B = A[0], B[0]

        if first_element_A > first_element_B:
            return [first_element_A] + merge(A[1:], B)

        if first_element_B > first_element_A:
            return [first_element_B] + merge(A, B[1:])
    
    if len(array) == 1:
        return array
    
    midpoint = len(array)//2
    return merge(mergesort(array[:midpoint]), mergesort(array[midpoint+1:]))

