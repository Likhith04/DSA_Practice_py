def isSorted(a):
    l = len(a)

    if l == 0 or l == 1:
        return True
    
    if a[0] > a[1]:
        return False

    smallerList = a[1:] # Copying the list and checking
    is_Smaller_Sorted = isSorted(smallerList)

    return is_Smaller_Sorted

def isSortedBetter(a,si):
    l = len(a)

    if si==l or si==l-1:
        return True
    if a[si] > a[si+1]:
        return False
    
    isSmaller_sorted = isSortedBetter(a,si+1)
    return isSmaller_sorted


a = [1,2,8,4,5]

print(isSortedBetter(a,0))

