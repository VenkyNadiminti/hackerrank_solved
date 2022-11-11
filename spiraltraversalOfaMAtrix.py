for _ in range(int(input())):
    n=int(input())
    mat=[[int(x) for x in input().split()] for z in range(n)]
    top,bottom,left,right,d=0,n-1,0,n-1,0
    while top<=bottom and left<=right:
        if d==0:
            i=left
            while i<=right:
                print(mat[top][i],end=" ")
                i+=1
            top=top+1
        elif d==1:
            i=top
            while i<=bottom:
                print(mat[i][right],end=" ")
                i+=1
            right-=1
        elif d==2:
            i=right
            while i>=left:
                print(mat[bottom][i],end=" ")
                i-=1
            bottom-=1
        elif d==3:
            i=bottom
            while i>=top:
                print(mat[i][left],end=" ")
                i-=1
            left+=1
        d=(d+1)%4
    print()
