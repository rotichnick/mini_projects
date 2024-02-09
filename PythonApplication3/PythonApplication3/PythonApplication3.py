
L=[12,3,45,6,87,9]

lower=0
upper=len(L)
for x in range(lower+1, upper):
    print(x, L[x])
    item=L[x]
    curr=x-1
    while L[curr]>item and curr>=0:
        L[curr], L[curr+1]=L[curr+1], L[curr]
        curr=-1
    L[curr+1]=item

print(L)
