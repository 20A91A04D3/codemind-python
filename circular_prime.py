def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def rev(n):
    s=0
    l=len(str(n))
    while n:
        a=n%10
        s=s+a*(10**(l-1))
        l-=1
        n=n//10
    return s
n=int(input())
n1=rev(n)
if prime(n)==prime(n1)==True:
    print('circular prime')
elif prime(n)==True:
    print('prime but not a circular prime')
elif prime(n1)==True:
    print('prime but not a circular prime')
else:
    print('not prime')