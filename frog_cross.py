def n_jumps_oneliner(X, Y, D):
    
    return (Y-X) // D if ((Y-X) % D == 0) else ((Y-X) // D) + 1

def n_jumps_readable(X, Y, D):
    floor = (Y-X) // D
    rem = (Y-X) % D
    if rem == 0:
        return floor
    else:
        return floor + 1

def n_jumps_loop(X, Y, D): # this algo is correct, but inneficient (O(Y-X))
    jumps = 0
    while X < Y:
        X = X + D # jump
        jumps += 1
    return jumps