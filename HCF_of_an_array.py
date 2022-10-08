n=int(input())
d=list(map(int,input().split()))
a=min(d)
c=0
for i in d:
    if i%a==0:
        c+=1
if c==n:
    print(a)
else:
    print('1')