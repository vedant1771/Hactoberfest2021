def weightedMean(v,m):
    c=0
    d=0
    h=0
    for i in range(0,n):
        s=v[i]*m[i]
        d=d+s

    for j in range(0,n):
        c=c+m[j]

    m=d/c
    return(m)

l=[]
n=int(input())
vals = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))
s=weightedMean(vals, weights)
print('%0.1f' %s)
