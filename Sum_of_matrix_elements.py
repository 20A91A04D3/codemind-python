n=int(input())
m=int(input())
s=0
while n:
    d=list(map(int,input().split()))
    s=s+sum(d)
    n-=1
print(s)
    