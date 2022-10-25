def diagonalDifference(arr):
    '''
    calculate the absolute difference between the sums of its diagonals.

    args:
    int arr[n][m]: an array of integers, n=m

    Return
    int: the absolute diagonal difference
    Input Format

    '''
    N = len(arr)-1
    diff = 0
    for i,row in enumerate(arr):
        print(row[i],row[N-i])
        diff += row[i]-row[N-i]
    return abs(diff)