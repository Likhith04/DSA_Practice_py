def is_Present(a,x,si):
    
    if si == len(a):
        return -1


    if a[si] == x:
        return si

    smallerListOutput = is_Present(a,x,si+1)
    return smallerListOutput

a =[1,2,3,4,5]
print(is_Present(a,10,0))
