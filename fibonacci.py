def fab(n):
    c=2
    a=0
    b=1
    print(a,b,end=' ')
    k=n
    while k:
        m=a+b
        c+=1
        if c==n:
            return m
        print(m,end=' ')
        a=b
        b=m
n=int(input())
print(fab(n))