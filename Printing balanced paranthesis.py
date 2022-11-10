#add "{" only if openN<n
#add "}" only if closeN<openN
#valid only iff openN==closeN==n

def generate(n,openN,closeN):
    if openN== closeN == n:
        res.append("".join(stack))
        return
    if openN<n:
        stack.append("{")
        generate(n,openN+1,closeN)
        stack.pop()
    if closeN<openN:
        stack.append("}")
        generate(n,openN,closeN+1)
        stack.pop()
    return res
for i in range(int(input())):
    n=int(input())
    stack=[]
    res=[]
    res=generate(n,0,0)
    print(f'Test Case #{i+1}:')
    for i in res:
        print(i)
