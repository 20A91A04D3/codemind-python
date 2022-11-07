n=int(input())
s=0
while n:
    a=n%10
    s=s+a
    n=n//10
    if n==0 and s>9:
        n=s
        s=0
print(s)