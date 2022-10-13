n=int(input())
d=list(map(int,input().split()))
d=sorted(list(set(d)))
for i in range(len(d)):
    print(d[i],end=' ')