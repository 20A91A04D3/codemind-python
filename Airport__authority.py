n=int(input())
d=[]
while n:
    a=int(input())
    d.append(a)
    n-=1
w=int(input())
c=0
for i in d:
    if i<=w:
        c+=1
    else:
        c+=2
print(c)
    