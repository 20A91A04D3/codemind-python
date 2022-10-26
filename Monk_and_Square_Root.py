def monk(a,b):
    c=0
    while c+1:
        if (c*c)%b==a:
            return c
        if c==b:
            return -1
        c+=1
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a>=b:
        print('-1')
    else:
        print(monk(a,b))