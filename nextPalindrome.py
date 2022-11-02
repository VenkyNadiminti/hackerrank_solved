def allNines(num):                     #TC:O(n),SC:O(1)
    for i in range(len(num)):
        if num[i]!='9' :
            return False
    return True

def allZeros(num):
    for i in range(len(num)):
        if num[i]!='0':
            return False
    return True


    
def nextpalindrome(num,l):
    num_arr=list(num)
    if allZeros(num):
        if len(num)==1:
            print(1)
            return
        print(f'1{"0"*(len(num)-2)}1')
        return
        

    if allNines(num):
        print(f'1{"0"*(len(num)-1)}1')
        return
        
        
    leftP=len(num)//2
    rightP=len(num)//2
    if len(num)%2==0:
        leftP-=1
    while leftP>=0 and num[leftP]==num[rightP]:
        leftP-=1
        rightP+=1
    if leftP<0 or num[leftP]<num[rightP]:
        leftP=len(num)//2
        rightP=len(num)//2
        if len(num)%2==0:
            leftP-=1
        carry=1
        while(leftP>=0):
            number=(int(num[leftP]))+carry
            carry=number//10
            num_arr[leftP]=str(number%10)
            num_arr[rightP]=num_arr[leftP]
            leftP-=1
            rightP+=1
    else:
        while(leftP>=0):
            num_arr[rightP]=num_arr[leftP]
            leftP-=1
            rightP+=1
    print("".join(num_arr))
        
        
    
for i in range(int(input())):
    n=input()
    nextpalindrome(n,len(n))
