n=int(input())
d=list(map(int,input().split()))
a=[]
m=min(d)
c=0
x=0
for i in range(1,m+1):
    if m%i==0:
        a.append(i)
for i in a:
    x=0
    for j in d:
        if j%i==0:
            x+=1
    if x==n:
        c=i
print(c)
            
