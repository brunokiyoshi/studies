def array_equilibrium(A):
    N = len(A)
    total = sum(A)
    min = float("inf")
    left = A[0]
    right = total - left
    min = abs(right-left)
    # the array cannot be broken on the first or last position
    # so iterate over the middle [1,N-1[
    for x in A[1:N-1]: 
        left = left + x
        right = right - x
        diff = abs(right-left)
        if diff < min: min=diff
    return min

def return_equilibrium_breakage_point(A):
    N = len(A)
    min = float("inf")
    left = A[0]
    right = sum(A[1:])
    min = abs(right-left)
    P=1
    # the array cannot be broken on the first or last position
    # so iterate over the middle [1,N-1[
    
    for x in A[1:N-1]: 
        left = left + x
        right = right - x
        diff = abs(right-left)
        if diff < min:
            min=diff
            Pmin = P + 1
        P += 1
    return Pmin