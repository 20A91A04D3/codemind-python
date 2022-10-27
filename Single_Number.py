n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    c=c^i
print(c)