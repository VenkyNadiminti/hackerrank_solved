for _ in range(int(input())):
    n=int(input())
    mat=[[int(x) for x in input().split()][::-1] for x in range(n)]
    for x in range(2*n-1):
        s=0
        for y in range(n):
            for z in range(n):
                if y+z==x:
                    s+=mat[y][z]
        print(s,end=" ")   
    print() 
