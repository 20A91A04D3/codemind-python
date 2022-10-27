a,b=map(int,input().split())
d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
c=0
for i in d2:
    if i in d1:
        c+=1
        d1.remove(i)
if c==b:
    print('Yes')
else:
    print('No')