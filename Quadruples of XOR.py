from bisect import bisect_left,bisect_right
def solve(a,b,c,d,x,n):
    count=0
    v1,v2=[],[]
    for i in range(n):
        for j in range(n):
            v1.append(a[i]^b[j])
            v2.append(x^c[i]^d[j])
    v1.sort()
    for i in range(len(v2)):
        low=bisect_left(v1,v2[i])
        high=bisect_right(v1,v2[i])
        count+=high-low
    return count

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    d=list(map(int,input().split()))
    print(solve(a,b,c,d,0,n))
    
