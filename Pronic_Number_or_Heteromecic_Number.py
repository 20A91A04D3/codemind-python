def pro(n):
    a=0
    b=a+1
    while b<=n:
        if a*b==n:
            return 'YES'
        a=b
        b=a+1
    return 'NO'
n=int(input())
print(pro(n))