n=int(input())
d=list(map(int,input().split()))
s=[]
for i in d:
    if d.count(i)==1:
        s.append(i)
s=sorted(list(set(s)))
for i in s:
    print(i,end=' ')