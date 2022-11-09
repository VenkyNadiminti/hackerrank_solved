for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    for i in range(n):
        ans^=l[i]+l[i]
    print(ans)
    
    
    
