d1=list(map(int,input().split()))
d2=list(map(int,input().split()))
a=0
b=0
for i in range(len(d1)):
    if d1[i]>d2[i]:
        a+=1
    elif d1[i]<d2[i]:
        b+=1
print(a,b)