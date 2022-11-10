def generate(arr):
    res=[]
    for i in range(1,1<<len(arr)):
        ans=[]
        for j in range(0,len(arr)):
            if i&(1<<j):
                ans.append(arr[j])
        res.append(ans)
    res.sort()
    return res
for z in range(int(input())):
    s=int(input())
    l=list(map(int,input().split()))
    ans=generate(sorted(l))
    for i in ans:
        for j in i:
            print(j,end=" ")
        print()
    print()
