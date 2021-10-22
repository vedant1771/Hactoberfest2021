t=int(input())
while(t!=0):
    n=int(input())
    N=list(map(int,input().split()))
    K=int(input())
    x=N[K-1]
    N.sort()
    print(N.index(x)+1)
    
    t=t-1