def fab(n):
    a=1
    b=2
    while n:
        c=a+b
        a=b
        b=c
        if c==n:
            return True
        if c>n:
            return False
n=int(input())
print(fab(n))