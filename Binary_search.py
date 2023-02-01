def binary_search(a,x,si,ei):
    if si > ei:
        return -1
    
    mid = (si+ei)//2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binary_search(a,x,si,mid-1)
    else :
        return binary_search(a,x,mid+1,ei)

a = [1,3,5,7,9,11]

print(binary_search(a,2,0,5))