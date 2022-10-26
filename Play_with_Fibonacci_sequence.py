def fab(n):
    a=0
    b=1
    count=2
    print(a,b,end=' ')
    while count:
        c=a+b
        count+=1
        if count==n:
            return c
        print(c,end=' ')
        a=b
        b=c
n=int(input())
print(fab(n))
