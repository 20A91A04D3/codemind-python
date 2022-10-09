a,b=map(int,input().split())
c=0
for i in range(max(a,b),a*b+1):
    if i%a==0 and i%b==0:
        c=i
        break
print(c)