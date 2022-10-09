n=int(input())
m=0
while n:
    a=n%10
    if a>m:
        m=a
    n=n//10
print(m)