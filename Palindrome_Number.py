def pal(n):
    if n<0:
        return False
    a=n
    s=0
    l=len(str(a))
    while n:
        x=n%10
        s=s+x*(10**(l-1))
        l-=1
        n=n//10
    if s==a:
        return True
    else:
        return False
for _ in range(int(input())):
    a=int(input())
    print(pal(a))