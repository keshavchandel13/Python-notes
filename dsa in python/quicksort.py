def quicksort(a,p,r):
    if p<r:
        q = partiton(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
    return a

def partiton(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r-1):
        if a[j] <= x:
            i=i+1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i+1]
    a[i+1] = a[r]
    a[r]  = temp
    return i+1 
    
a = [66,33,22,55,89,70]
print(a)
b=quicksort(a,0,len(a)-1)
print(b)