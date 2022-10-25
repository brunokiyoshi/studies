from collections import Counter

def countingSort(arr): # obvious best

    out = [0]*100
    for x in arr:
        out[x]+=1
        
    return out

def countingSort_collections(arr):
    counter = Counter()
    counter.update(arr)
    out = [None]*100
    print(out)
    for i in range(0,100):
        print(i)
        out[i]=counter[i]
    return out

def countingSort_dict(arr):
    out_dict = {}
    for x in arr:
        out_dict.setdefault(x,0)
        out_dict[x] += 1
    out = [None]*100
    for i in range(0,100):
        out_dict.setdefault(i,0)
        out[i]=out_dict[i]
        
    return out