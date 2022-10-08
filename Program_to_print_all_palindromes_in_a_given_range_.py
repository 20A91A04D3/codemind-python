def pal(n):
    l=len(str(n))
    a=0
    d=n
    while d:
        m=d%10
        a=a+m*(10**(l-1))
        l-=1
        d=d//10
    return a
n=int(input())
m=int(input())
for i in range(n,m+1):
    if i==pal(i):
        print(i,end=' ')