n=int(input())
d=list(map(int,input().split()))
for i in d:
    c=d.count(i)
    if c>1:
        print(i)
        break