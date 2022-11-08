def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a=int(input())
b=int(input())
c=a+b
i=1
while c:
    k=c+i
    if prime(k)==True:
        print(i)
        break
    i+=1