t=int(input())
while(t!=0):
    n=int(input())
    S=list(map(int,input().split()))
    S.sort()
    diff=S[1]-S[0]
    for i in range(1,len(S)):
        if (S[i]-S[i-1]<diff):
            diff=S[i]-S[i-1]
    print(diff)
    
    t=t-1