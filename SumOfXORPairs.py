def xorsum(l,n):
    s=0
    for i in range(32):
        zeros=0
        ones=0
        idsum=0
        for j in range(n):
            if l[j]%2==0:
                zeros+=1
            else:
                ones+=1
            l[j]//=2
        idsum=zeros*ones*(1<<i)
        s=s+idsum
    return s
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    print(xorsum(l,n)*2)
    
