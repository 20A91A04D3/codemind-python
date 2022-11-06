def pal(n):
    l=len(str(n))
    a=n
    s=0
    while n:
        x=n%10
        s=s+x*10**(l-1)
        l-=1
        n=n//10
    if s==a:
        return True
    return False
def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
while n:
    n+=1
    if pal(n)==True and prime(n)==True:
        print(n)
        break