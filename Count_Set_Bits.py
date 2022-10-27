for _ in range(int(input())):
    n=int(input())
    a=bin(n)[2:]
    d=list(a)
    c=0
    for i in d:
        if i=='1':
            c+=1
    print(c)