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
print(rev(n))