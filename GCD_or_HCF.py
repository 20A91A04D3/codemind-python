def fact(m,M):
    c=1
    for i in range(1,m+1):
        if m%i==0 and M%i==0:
            c=i
    return c
a,b=map(int,input().split())
m=min(a,b)
M=max(a,b)
if M%m==0:
    print(m)
else:
    print(fact(m,M))
    