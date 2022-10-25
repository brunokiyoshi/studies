def one_occurrence_in_array(A): # this assumes unpaired element appears exactly once in array

    A.sort() # probably the most costly part of the algo. Anything below this will be O(n)
    N = len(A)
    # cover cases where unpaired element is in first position
    if N == 1: return A[0] # singleton case
    if A[0] != A[1]: return A[0] # if second element differs from first, first is unpaired
    # cover middle
    for i in range(2, N-2):
        xl,x = A[i-1], A[i]
        if xl != x:
            xr = A[i+1]
            if xr != x:
                return x 
    # cover cases where unpaired is the last element
    # if code reaches this point, unpaired element is not in the middle 
    return A[-1]

def odd_occurrences_in_array(A): # this scored 66%
    # this considers unpaired number can appear any odd number of times instead of only 1
    A.sort() # probably the most costly part of the algo. Anything below this will be O(n)
    N = len(A)
    # cover cases where unpaired element is in first position
    if N == 1: return A[0] # singleton case
    count = 1
    for i in range(1, N):
        xl,x = A[i-1], A[i]
        if xl == x:
            count += 1
        else:
            if count % 2 == 0:
                count = 1
            else:
                return xl
    return x # if code reached this point, the last number appears an odd number of times