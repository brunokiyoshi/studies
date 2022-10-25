def cyclic_rotation_recursive(A, K):
    """ Takes a list A and rotates it K times.
        Rotation means that each element is shifted right by one index,
        and the last element of the array is moved to the first place.
    """
    A.append(None) # add one element to A which acts as auxiliary variable
    i = len(A) - 1
    while i >= 0:
        A[i] = A[i-1]
        i -= 1
    A = A[:-1]
    K -= 1
    if K > 0:
        return cyclic_rotation_recursive(A,K)
    else:
        return A

def cyclic_rotation(A, K):
    """ Takes a list A and rotates it K times.
        Rotation means that each element is shifted right by one index,
        and the last element of the array is moved to the first place.
    """
    if len(A) > 0:
        while K > 0:
            aux = A[-1]
            i = len(A) - 1
            while i > 0:
                A[i] = A[i-1]
                i -= 1
            A[0] = aux
            K -= 1
    return A