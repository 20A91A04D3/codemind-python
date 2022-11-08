a,b=map(int,input().split())
p=0
while a:
    s=b
    while s:
        d=list(map(int,input().split()))
        p+=sum(d)
        s-=s
    a-=1
print(p)
    