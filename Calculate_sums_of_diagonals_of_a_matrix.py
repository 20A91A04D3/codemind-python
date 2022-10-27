n=int(input())
d=0
r=n-1
d1=0
r1=0
while n:
    m=list(map(int,input().split()))
    d1=d1+m[d]
    r1=r1+m[r]
    n-=1
    d+=1
    r-=1
print('Principal Diagonal:',end='')
print(d1)
print('Secondary Diagonal:',end='')
print(r1)